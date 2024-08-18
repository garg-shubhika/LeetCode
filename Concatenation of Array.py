class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        k = 0
        for i in range(2*len(nums)+1):
            if k<len(nums):
                ans.append(nums[k])
                k = k+1
            else:
                k = 0
        return ans
