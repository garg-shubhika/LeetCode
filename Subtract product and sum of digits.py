class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        s = 0
        k = 1
        for i in num:
            k = k*(int(i))
            s = s+(int(i))
        return (k-s)
