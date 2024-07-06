# Fibonacci series
class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        for i in range(n):
            sum = x + y
            x = y
            y = sum
        return sum
