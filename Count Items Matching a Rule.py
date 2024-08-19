class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        k = 0
        d = {}
        for i in items:
            d["type"] = i[0]
            d["color"] = i[1]
            d["name"] = i[2]
            if(d[ruleKey]==ruleValue):
                k = k+1
        return k
