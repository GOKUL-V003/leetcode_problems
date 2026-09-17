class Solution:
    def majorityElement(self, a: List[int]) -> int:
        d={}
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            return (max(d,key=d.get))