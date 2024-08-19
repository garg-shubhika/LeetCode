class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e = []
        o = []
        o = sorted(nums[::2])
        e =sorted(nums[1::2],reverse=True)
        l = []
        for i in range(len(nums)//2):
            l.append(o[i])
            l.append(e[i])
        if len(nums)%2!=0:
            l.append(o[-1])
        return l
