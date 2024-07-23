class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        c = 0
        n = num
        o = 1
        while n>0:
            n = n-o
            o = o+2
            c = c+1
        if c*c == num:
            return True
        else:
            return False


# the square root of 16 using this method.

#16 - 1 = 15
#15 - 3 =12
#12 - 5 = 7
#7- 7 = 0
#We have subtracted 4 times. Thus,√16 = 4
