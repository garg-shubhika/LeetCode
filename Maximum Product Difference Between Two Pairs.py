class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        l = len(nums)
        #print(nums)
        k = (nums[0]*nums[1]) - (nums[l-1]*nums[l-2])
        return k
