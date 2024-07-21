class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x = sorted(list(s))
        y = sorted(list(t))
        for i in range(len(x)):
            if y[i]!=x[i]:
                return y[i]
        return y[-1]
        
