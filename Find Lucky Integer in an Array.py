class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s = 0
        maxi = -1
        for i in arr:
            s = arr.count(i)
            if i == s:
                if s>maxi:
                    maxi = s
        return maxi
