class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ind = 0
        max_val = 0
        for i,j in enumerate(mat):
            if j.count(1) > max_val:
                max_val = j.count(1)
                ind = i
        return [ind,max_val]
