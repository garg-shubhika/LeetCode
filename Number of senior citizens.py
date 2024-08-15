class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = []
        c = 0
        for i in details:
            temp = i
            r = temp[11]+temp[12]
            if int(r)>60:
                c = c+1
        return c
