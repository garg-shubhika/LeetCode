class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        k = list(set(nums))
        k.sort()
        print(k)
        if k!=nums:
            return True
        else:
            return False
