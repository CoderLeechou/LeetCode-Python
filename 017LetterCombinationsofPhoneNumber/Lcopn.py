#-*-coding:utf-8-*-
import copy
class Solution(object):
    #方法1，利用字典dict，使用递归
    """""
    def letterCombinations(self,digits):
        def dfs(num,string,res):
            if num==length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                dfs(num+1,string+letter,res)
        dict={'2': ['a', 'b', 'c'],
              '3': ['d', 'e', 'f'],
              '4': ['g', 'h', 'i'],
              '5': ['j', 'k', 'l'],
              '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r','s'],
              '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y','z']}
        res=[]
        length=len(digits)
        if length==0:
            return res
        dfs(0,'',res)
        return res
    """
    #方法2，使用字符串数组加三重循环
    def letterCombinations(self,digits):
        chr=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res=[]
        for i in range(0,len(digits)):
            num=int(digits[i])
            tmp=[]
            for j in range(0,len(chr[num])):
                if len(res):
                    for k in range(0,len(res)):
                        tmp.append(res[k]+chr[num][j])
                else:
                    tmp.append(str(chr[num][j]))
            res=copy.copy(tmp)
        return res
if __name__=='__main__':
    dig="23"
    print Solution().letterCombinations(dig)