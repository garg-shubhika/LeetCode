class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        k = dict(zip(heights,names))
        m = dict(sorted(k.items(),reverse=True))
        l = list(m.values())
        return l
