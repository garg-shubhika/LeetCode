class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n,n*10):
            if i%2 == 0 and i%n == 0:
                return i
