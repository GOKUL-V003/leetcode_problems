class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a = title.lower().split()

        for i in range(len(a)):
            if len(a[i]) > 2:
                a[i] = a[i].capitalize()

        return " ".join(a)