class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        n = nums
        l = len(n)
        for i in range(len(n)):
            s = n[i] + n[l-1-i]
            averages.append(s/2)
        return min(averages)
