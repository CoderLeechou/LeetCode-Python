#-*-coding:utf-8-*-
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution(object):
    def reverseKGroup(self,head,k):
        ans=ListNode(0)
        if head==None:
            return None
        ans.next=head
        start=ans
        while start.next!=None:
            end=start
            i=0
            while i<k-1:
                end=end.next
                if end.next==None:
                    return ans.next
                i+=1
            tmp=self.reverse(start.next,end.next)
            start.next=tmp[0]
            start=tmp[1]
        return ans.next
    def reverse(self,start,end):
        nhead=ListNode(0)
        nhead.next=start
        while nhead.next!=None:
            tmp=start.next
            start.next=tmp.next
            tmp.next=nhead.next
            nhead.next=tmp
        return [end,start]