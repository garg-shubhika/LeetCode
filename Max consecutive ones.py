class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max = 0
        for i in nums:
            if i ==1:
                c = c+1
            else:
                c = 0
            if c>max:
                max = c
        return max
