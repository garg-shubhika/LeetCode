class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m = set(range(1,len(arr)+k+1))
        r = sorted(list(m-set(arr)))
        #print(m)
        #print(r)
        #print(r[k-1])
        #print(m)
        return r[k-1]
