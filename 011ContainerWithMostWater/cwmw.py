#-*-coding:utf-8-*-
class Solution(object):
    """
    def maxArea(self,height):
        size=len(height)
        maxw=0
        l,r=0,size-1
        while l<r:
            if height[l]<=height[r]:
                maxw=max(maxw,height[l]*(r-l))
                l+=1
            else:
                maxw=max(maxw,height[r]*(r-l))
                r-=1
        return maxw

    def maxArea(self,height):
        size=len(height)
        maxw=0
        l,r=0,size-1
        while l<r:
            maxw=max(maxw,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxw
    """
    def maxArea(self,height):
        size=len(height)
        maxw=0
        l,r=0,size-1
        while l<r:
            maxw=max(maxw,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                k=l
                while k<r and height[k]<=height[l]:
                    k+=1
                l=k
            else:
                k=r
                while k>l and height[k]<=height[r]:
                    k-=1
                r=k
        return maxw


if __name__=='__main__':
    height=[1,2]
    print Solution().maxArea(height)