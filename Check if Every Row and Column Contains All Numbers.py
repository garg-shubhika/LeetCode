class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        c = len(matrix)
        #print(c)
        count = {}
        for i in matrix:
            d = set(i)
            for j in i:
                if j>c:
                    return False
            if len(d)!=c:
                return False
        for i in zip(*matrix):
            d = set(i)
            for j in i:
                if j>c:
                    return False
            if len(d)!=c:
                return False
        return True
