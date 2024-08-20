class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            a = []
            for j in str(i):
                a.append(j)
            if len(a)%2==0:
                c=c+1
        return c
