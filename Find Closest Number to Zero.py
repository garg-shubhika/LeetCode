class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        dif = []
        for i in nums:
            dif.append(abs(i-0))
        d = dict(zip(nums,dif))
        #sorted(d,reverse=True)
        print(d)
        for key, val in d.items():
            if val==min(d.values()):
                return key
        #print(s)
        return 0

