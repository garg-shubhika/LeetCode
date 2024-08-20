class Solution:
    def scoreOfString(self, s: str) -> int:
        s1 = 0
        j = []
        for i in s:
            j.append(ord(i))
        for k in range(len(j)-1):
            s1 = s1 + abs(j[k]-j[k+1])
        print(s1)
        return s1
