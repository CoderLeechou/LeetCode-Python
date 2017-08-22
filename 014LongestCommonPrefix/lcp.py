#-*-coding:utf-8-*-
class Solution(object):
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return ''
        if len(strs)==1:
            return strs[0]
        end,minl=0,min([len(s) for s in strs])
        while end<minl:
            for i in range(1,len(strs)):
                if strs[i][end]!=strs[i-1][end]:
                    return strs[0][:end]
            end+=1
        return strs[0][:end]
if __name__=='__main__':
    strs=['abc','abd','ab']
    print Solution().longestCommonPrefix(strs)
