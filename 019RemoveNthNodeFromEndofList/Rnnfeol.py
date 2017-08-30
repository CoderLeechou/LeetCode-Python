#-*-coding:utf-8-*-
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def removeNthFromEnd(self,head,n):
        res=ListNode(0)
        res.next=head
        tmp=res
        for i in range(0,n):
            head= head.next
        while head!=None:
            head=head.next
            tmp=tmp.next
        tmp.next=tmp.next.next
        return res.next
