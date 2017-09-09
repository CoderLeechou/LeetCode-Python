#-*-coding:utf-8-*-
class Solution(object):
    def removeDuplicates(self,nums):
        i = 1
        j = 1
        size = len(nums)
        while j < size:
            if nums[j] == nums[i - 1]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        return min(i, size)
if __name__=='__main__':
    nums=[2,3,3,4,4]
    len=Solution().removeDuplicates(nums)
    print len
    for i in range(0,len):
        print nums[i]