class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        x = []
        cou = 0
        for i in range(m):
            r = []
            for j in range(n):
                r.append(0)
            x.append(r)
        for j in indices:
            for i in range(n):
                x[j[0]][i]+=1
            for i in range(m):
                x[i][j[1]]+=1
        for i in range(m):
            for j in range(n):
                if x[i][j]%2==1:
                    cou = cou+1
        return cou

        return 0
