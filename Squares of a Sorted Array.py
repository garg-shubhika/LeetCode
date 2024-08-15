class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x = []
        c = len(nums)
        for i in range(0,c):
            x.append(nums[i]*nums[i])
        x.sort()
        return x
