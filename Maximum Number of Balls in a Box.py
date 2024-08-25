class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = range(lowLimit, highLimit+1)
        l = [0]*(lowLimit+highLimit)
        
        for i in n:
            s = sum([int(i) for i in str(i)])
            l[s]+=1
        return max(l)
