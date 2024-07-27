class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        s = []
        for i in range(left,right+1):
            c = 0
            for j in str(i):
                if j=='0' or i%int(j)!=0:
                    c = 1
            if c == 0:
                s.append(i)
        return s
