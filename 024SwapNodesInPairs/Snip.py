#—*-coding:utf-8-*-
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def swapPairs(self,head):
        if head==None or head.next==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next and p.next.next:
            tmp=p.next.next
            p.next.next=tmp.next
            tmp.next=p.next
            p.next=tmp
            p=p.next.next
        return dummy.next
