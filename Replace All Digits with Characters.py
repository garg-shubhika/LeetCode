class Solution:
    def replaceDigits(self, s: str) -> str:
        l =''
        for i in range(len(s)):
            if i%2!=0:
                k = ord(s[i-1])
                l = l + (chr(k+int(s[i])))
            else:
                l = l+s[i]
        return l
