class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        nums.sort()
        c = 0
        for i in range(l):
            for j in range(i+1,l):
                if abs(nums[i]-nums[j])==k:
                    c = c+1
        print(c)
        return c
