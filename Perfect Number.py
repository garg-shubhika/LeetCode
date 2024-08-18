class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        l = int(num**0.5+1)
        for i in range(2,l):
            if num%i==0:
                s = s+i
                s = s+(num/i)
            print(num,i,s)
           
        if s==num and num!=1:
            return True
        else:
            return False
