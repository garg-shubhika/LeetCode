class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=[]
        if (len(word1)==len(word2)):
            x = list(word1)
            y = list(word2)
            for i in range(len(word1)):
                s.append(x[i])
                s.append(y[i])
            return "".join(s)
        else:
            x = list(word1)
            y = list(word2)
            l = min(len(word1),len(word2))
            max_len = max(len(word1),len(word2))
            for i in range(l):
                s.append(x[i])
                s.append(y[i])
            if len(word1)==max_len:
                print("word1")
                s.append(word1[l:])
            else:
                s.append(word2[l:])
            return "".join(s)
