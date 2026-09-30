class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        d = {}

        for i in ranks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        if len(set(suits)) == 1:
            return "Flush"

        for i in d:
            if d[i] >= 3:
                return "Three of a Kind"

        for i in d:
            if d[i] >= 2:
                return "Pair"

        return "High Card"