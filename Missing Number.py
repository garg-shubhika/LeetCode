class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)+1
        for j in range(0,l):
            if j not in nums:
                return j
