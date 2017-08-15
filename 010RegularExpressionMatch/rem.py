#-*-coding:utf-8-*-
import re
class Solution(object):
    #方法一，直接使用正则表达式
    """""
    def isMatch(self,s,p):
        return re.match(p+'$',s)!=None
        """
    #方法2，DP
    def isMatch(self,s,p):
        match=[]
        for i in range(0,len(s)+1):
            #match.insert(i,False)
            match.append(False)
        match[len(s)]=True
        j=len(p)-1
        while j>=0:
            if p[j]=='*':
                k=len(s)-1
                while k>=0:
                    match[k]=match[k] or match[k+1] and (p[j-1]=='.' or s[k]==p[j-1])
                    k-=1
                j-=1
            else:
                m=0
                while m<len(s):
                    match[m]=match[m+1] and (p[j]=='.' or p[j]==s[m])
                    m+=1
                match[len(s)]=False
            j-=1
        return match[0]

if __name__=='__main__':
    s='ab'
    p='.*'
    print Solution().isMatch(s,p)