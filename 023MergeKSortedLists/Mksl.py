#-*-coding:utf-8-*-
class ListNode(object):
    def __init__(self,x):
        self.val=x;
        self.next=None
#方法1，有例子不通过
class Solution(object):
    def mergeKLists(self,lists):
        size=len(lists)
        if size==0:
            return None
        if size==1:
            return list[0]
        n=size//2
        tmp1=self.mergeKLists(lists[:n])
        tmp2=self.mergeKLists(lists[n:])
        return self.mergeTwoLists(tmp1,tmp2)

    def mergeTwoLists(self,l1,l2):
        ans=ListNode(0)
        tmp=ans
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                tmp.next=l1
                l1=l1.next
            else:
                tmp.next=l2
                l2=l2.next
            tmp=tmp.next
        if l1!=None:
            tmp.next=l1
        else:
            tmp.next=l2
        return ans.next


from heapq import heappop, heappush


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
            trav = dummy = ListNode(-1)
            heap = []
        for ll in lists:
            if ll:
                self.heappushNode(heap, ll)
        while heap:
            node = heappop(heap)[1]
            trav.next = node
            trav = trav.next
            if trav.next:
                self.heappushNode(heap, trav.next)
        return dummy.next
    def heappushNode(self, heap, node):
        heappush(heap, (node.val, node))
