class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        m = []
        for i,j in enumerate(words):
            if x in j:
                m.append(i)
        return m
