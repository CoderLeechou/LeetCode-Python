#-*-coding:utf-8=*-
class Solution(object):
      """""
      def convert(self,s,numRows):
        size=len(s)
        if size<=numRows or numRows==1:
            return s
        ans=''
        i=0
        while i<numRows:
            j=i
            if i==0 or i==numRows-1:
                while j<size:
                    ans +=s[j]
                    j+=2*numRows-2
                    if 2*numRows-2==0:
                        break
            else:
                while j<size:
                    ans+=s[j]
                    j+=2*(numRows-i)-2
                    if j>=size:
                        break
                    ans+=s[j]
                    j+=2*i
            i+=1
        return ans
        """
      def convert(self, s, numRows):
          size = len(s)
          if size <= numRows or numRows == 1:
              return s
          ans = ''
          num = 2*numRows-2
          i=0
          while i<numRows:
              j=i
              while j<size:
                  ans+=s[j]
                  if i!=0 and i!=numRows-1:
                      temp=j+num-2*i
                      if temp<size:
                          ans+=s[temp]
                  j+=num
              i+=1
          return ans
if __name__=='__main__':
    s='PAYPAWZ'
    print Solution().convert(s,3)