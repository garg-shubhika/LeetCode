class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s = 0
        nums = [start]
        for i in range(n):
            nums.append(start+2*i)
        nums.remove(nums[0])
        for j in nums:
            s = s^j
        #print(s)
        return s
