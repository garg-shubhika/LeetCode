class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        m = []
        c=[]
        for i in nums:
            if i%2==0:
                m.append(i)
                c.append(nums.count(i))
        #print(m)
        #print(c)
        d = dict(zip(m,c))
        for key,val in d.items():
            if val==max(d.values()):
                return key
        #print(d)
        return -1
