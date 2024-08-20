class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = 0
        x = []
        for i in arr:
            c = arr.count(i)
            x.append(c)
        d =dict(zip(arr,x))
        m = []
        for key, val in d.items():
            m.append(val)
        r = list(set(m))
        
        r.sort()
        m.sort()
        print(m)
        print(r)
        if r==m:
            return True
        else:
            return False
