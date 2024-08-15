class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        x =[]
        for i in nums:
            for j in str(i):
                x.append(int(j))
        return x
