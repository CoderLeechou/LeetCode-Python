#-*-coding:utf-8-*-
class Solution(object):
    def generateParenthesis(self,n):
        if n==0:
            return []
        res=[]
        self.helper(n,n,'',res)
        return res
    def helper(self,l,r,paren,res):
        if r<l:
            return
        if l==0 and r==0:
            res.append(paren)
        if l>0:
            self.helper(l-1,r,paren+'(',res)
        if r>0:
            self.helper(l,r-1,paren+')',res)
if __name__=='__main__':
    n=3
    print Solution().generateParenthesis(n)