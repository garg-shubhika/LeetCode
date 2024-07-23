class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = "{0:b}".format(n)
        c = 0
        for i in m:
            if i == '1':
                c = c+1
        return c
