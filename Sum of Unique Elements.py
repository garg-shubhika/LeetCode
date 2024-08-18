class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = 0
        freq = []
        for i in nums:
            c = nums.count(i)
            freq.append(c)
        d = dict(zip(nums, freq))
        for key, value in d.items():
            if value==1:
                s = s+key
            print(s)
        return s
