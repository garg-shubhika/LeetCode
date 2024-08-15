class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        for i in nums:
            if i!=a and i!=b:
                return i
        return -1
