#-*-coding:utf-8-*-
class Solution(object):
    def findMedianSortedArrays(self,nums1,nums2):
        n=len(nums1)+len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1,nums2,n / 2 + 1)
        else:
            smaller = self.findKth(nums1,nums2,n / 2)
            bigger = self.findKth(nums1,nums2,n / 2 + 1)
            return (smaller+bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a = A[k / 2 - 1] if len(A) >= k / 2 else None
        b = B[k / 2 - 1] if len(B) >= k / 2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[k / 2:], B, k - k / 2)
        return self.findKth(A, B[k / 2:], k - k / 2)

if __name__ == '__main__':
    nums1 = [1]
    nums2 = [3,4]
    a = Solution()
    print a.findMedianSortedArrays(nums1,nums2)