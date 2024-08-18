class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            for i in nums:
                if i==original:
                    original=original*2
        return original
