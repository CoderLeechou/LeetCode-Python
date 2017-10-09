class Solution(object):
    def strStr(self,haystack,needle):
        if haystack is None or needle is None:
            return -1;
        len_h=len(haystack)
        len_n=len(needle)
        for i in range(len_h-len_n+1):
            j=0
            while(j<len_n):
                if haystack[i+j]!=needle[j]:
                    break
                j+=1
            if j==len_n:
                return i
        return -1
if __name__=='__main__':
    haystack="abcda"
    needle="bc"
    r=Solution().strStr(haystack,needle)
    print r