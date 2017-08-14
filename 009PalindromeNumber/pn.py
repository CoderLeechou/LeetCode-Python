#-*-coding:utf-8-*-
class Solution(object):
  #方法1，反序比较
  """
  def isPalindrome(self,x):
    if x<0:
      return False
    b=x
    ans=0
    while x>0:
      ans=ans*10+x/10
      if x>2147483647:
        return False
      x//=10
    if ans==b:
      return True
    return False
  """
  #方法2，两端比较
  def isPalindrome(self,x):
    if x<0:
      return False
    div=1
    while div<=x/10:
      div*=10
    while x>0:
      if x/div!=x%10:
          return False
      x=(x%div)/10
      div//=100
    return True
if __name__=='__main__':
  x=12321
  print Solution().isPalindrome(x)
      
  
  
