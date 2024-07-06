class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        while n >= 10:
            s = 0
            while n > 0:
                digit = n % 10
                s += digit
                n = n // 10
            n = s
        return n
