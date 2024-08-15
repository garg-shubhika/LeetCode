class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = [0]
        for i in gain:
            x.append(x[-1]+i)
        return(max(x))
