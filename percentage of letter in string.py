class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = []
        for i in s:
            if i==letter:
                c.append(i)
        m = (len(c)/len(s))*100
        return int(m)
