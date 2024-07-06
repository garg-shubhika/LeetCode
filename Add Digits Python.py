class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        while(n>9):
            n = str(n)
            x = [int(i) for i in n]
            n = sum(x)
        return n
    
