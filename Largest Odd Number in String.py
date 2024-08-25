class Solution:
    def largestOddNumber(self, num: str) -> str:
        k = 0
        l = len(num)
        #####################
        for i in num:
            if int(i)%2==0:
                k = k+1
        if k==l:
            return ""

        #####################

        for i in range(l)[::-1]:
            if int(num[i])%2!=0:
                return num[:i+1]
