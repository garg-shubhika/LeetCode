class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        e = []
        for i in digits:
            e.append(str(i))
        y = int("".join(e))
        y = str(y+1)
        m = []
        for i in y:
            m.append(int(i))
        return m
            
