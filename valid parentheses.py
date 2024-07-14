class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        s = list(s)
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif i == ')' and len(stack)>0 and stack[-1]=='(':
                stack.pop()
            elif i == ']' and len(stack)>0 and stack[-1]=='[':
                stack.pop()
            elif i == '}' and len(stack)>0 and stack[-1]=='{':
                stack.pop()
            else:
                return False
        if stack ==[]:
            return True
        else:
            return False
