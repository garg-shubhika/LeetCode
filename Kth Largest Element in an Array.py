class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        #print(nums)
        #print(nums[k-1])
        return nums[k-1]
