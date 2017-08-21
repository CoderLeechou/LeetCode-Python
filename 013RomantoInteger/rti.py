#-*-coding:utf-8-*-
class Solution(object):
    #方法1，字典
    """""
    def romanToInt(self,s):
        ROMAN={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if s=="":
            return 0
        index=len(s)-2
        sum=ROMAN[s[-1]]
        while index>=0:
            if ROMAN[s[index]]<ROMAN[s[index+1]]:
                sum-=ROMAN[s[index]]
            else:
                sum+=ROMAN[s[index]]
            index-=1
        return sum
    """
    #方法2，我觉得最棒的
    def romanToInt(self,s):
        ans=0
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i=0
        while i<len(b):
           while s.find(b[i])==0:#不能用index,若b[i]不在，会报异常
               ans+=a[i]
               s=s[len(b[i]):]
           i+=1
        return ans


if __name__=='__main__':
    s='MCMXLI'
    print Solution().romanToInt(s)