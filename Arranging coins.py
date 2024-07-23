class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        i = 0
        c = 0
        while True:
            m = s
            t = i + 1
            s = m + t
            i = i+1
            c = c+1
            if s == n:
                return c
            elif s>n:
                return c-1
                
