class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums = list(set(nums))
        nums.sort(reverse=True)
        m = len(nums)
        if m>=3:
            return nums[2]
        else:
            return nums[0]
        
