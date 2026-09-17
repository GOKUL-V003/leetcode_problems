class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = []

        for i in range(len(names)):
            a.append([heights[i], names[i]])

        a.sort(reverse=True)

        result = []

        for i in a:
            result.append(i[1])

        return result