class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        a = sorted(nums1)
        b = sorted(nums2)
        x = []
        for i in range(len(a)):
            r = b[i] - a[i]
            x.append(r)   
        return x[0]