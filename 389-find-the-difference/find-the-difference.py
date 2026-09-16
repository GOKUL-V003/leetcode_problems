class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return i

            if d[i] == -1:
                return i