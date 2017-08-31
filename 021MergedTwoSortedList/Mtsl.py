#-*-coding:utf-8-*-
class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    #方法1，递归
    """""
    def mergeTwoLists(self,l1,l2):
        if l1==None:
            return l2
        if l2==None:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2
    """
    #方法2，非递归
    def mergeTwoLists(self,l1,l2):
        helper=ListNode(0)
        tmp=helper
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
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
        return helper.next