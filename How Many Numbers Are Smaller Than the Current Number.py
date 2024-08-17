class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = []
        for num in nums:
            l = [i for i in nums if i<num]
            s.append(len(l))
        return s
