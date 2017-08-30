#-*-coding:utf-8-*-
class Solution(object):
    def isValidParentheses(self,s):
        stack=[]
        for c in s:
            if c=='{' or c=='[' or c=='(':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c==']' and stack[-1]!='[' or c==')' and stack[-1]!='(' or c=='}' and stack[-1]!='{':
                    return False
                stack.pop()
        return not stack
if __name__=='__main__':
    s="([)]"
    print Solution().isValidParentheses(s)
