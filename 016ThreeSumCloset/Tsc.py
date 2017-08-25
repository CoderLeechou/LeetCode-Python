#-*-coding:utf-8-*-
class Solution(object):
    def threeSumCloset(self,nums,target):
        nums.sort
        ans=None
        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while(l<r):
                sum=nums[l]+nums[r]+nums[i]
                if ans is None or abs(sum-target)<abs(ans-target):
                    ans=sum
                if sum<=target:
                    l+=1
                else:
                    r-=1
        return ans
if __name__=='__main__':
    nums=[1,2,3,4,5]
    tar=5
    print Solution().threeSumCloset(nums,tar)