#-*-coding:utf-8-*-
class Solution(object):
    def reverse(self,x):
        pos=True
        if x<0:
           pos=False
        x=abs(x)
        ans=0
        while x>0:
            ans=ans*10+x%10
            x//=10
        if ans>2147483647:
            return 0
        if not pos:
            return -1*ans
        return ans
if __name__=='__main__':
     n=-321
     print Solution().reverse(n)

