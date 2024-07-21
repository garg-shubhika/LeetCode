class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        s = x+y
        m = "{0:b}".format(s)
        return m
