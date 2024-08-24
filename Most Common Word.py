class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        c = []
        for m in paragraph:
            if m in ',':
                paragraph = paragraph.replace(m," ")
            if m in '!?;,.\'"':
                paragraph = paragraph.replace(m,"")
        #print(paragraph)
        s = [word.lower() for word in paragraph.split()]
        for i in s:
            if i != banned:
                c.append(s.count(i))
        d1 = dict(zip(s,c))
        d = dict(sorted(d1.items()))
        str1 = ""
        banned_str = ','.join(banned)
        print(banned_str)
        #print(banned_str)
        banned_keys = banned_str.split(',')
        for key in banned_keys:
            if key in d:
                del d[key]
        for key,value in d.items() :
            #m = max(d.values())
            #print(i)
            if value==max(d.values()):
                    str1 = key
                    break
        print(str1)
        return str1
