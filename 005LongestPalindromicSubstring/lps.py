#-*-coding:utf-8-*-
class Solution(object):
    #时间太长
    """"
    def longestPalindrome(self,s):
        if not s or len(s) == 1:
            return s
        max_length = 1
        start_index = 0
        end_index = 0
        for i in range(0, len(s) - 1):
            count = 1
            # aba
            if s[i] != s[i + 1]:
                while i - count >= 0 and i + count < len(s) and s[i - count] == s[i + count]:
                    count += 1
                if (count - 1) * 2 + 1 > max_length:
                    max_length = (count - 1) * 2 + 1
                    start_index = i - count + 1
                    end_index = i + count - 1
                    # xaaaaax
            else:
                count_repeat = 1
                count = 0
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count_repeat += 1
                while i - count_repeat + 1 - count >= 0 and i + count < len(s) and s[i - count_repeat + 1 - count] == s[
                            i + count]:
                    count += 1
                if (count - 1) * 2 + count_repeat > max_length:
                    max_length = (count - 1) * 2 + count_repeat
                    start_index = i - count - count_repeat + 2
                    end_index = i + count - 1
        return s[start_index:end_index + 1]
    """
    def longestPalindrome(self,s):
        size=len(s)
        if size==1:
            return s
        if size==2:
            if s[0]==s[1]:
                return s
            return s[0]
        maxp=1
        ans=s[0]
        i=0
        while i<size:
            j=i+1
            while j<size:
                if s[i] == s[j]:
                    j+=1
                else:
                    break
            k=0
            while i-k-1>=0 and j+k<=size-1:
                if s[i-k-1]!=s[j+k]:
                    break
                k+=1
            if j-i+2*k>maxp:
                maxp=j-i+2*k
                ans=s[i-k:j+k]
            if j+k == size-1:
                break
            i=j
        return ans

if __name__=='__main__':
    s='abada'
    print Solution().longestPalindrome(s)
