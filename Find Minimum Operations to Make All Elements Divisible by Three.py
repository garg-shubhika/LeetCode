class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = len(nums)
        c = 0
        k = 0
        for i in nums:
            if i%3==0:
                c = c + 1
            else:
                k = k+1
        if c == l:
            return 0
        else:
            return k
