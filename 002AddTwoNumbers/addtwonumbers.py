#-*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=ListNode(0)
        tmp=ans
        tmpsum=0
        while True:
            if l1!=None:
                tmpsum+=l1.val
                l1=l1.next
            if l2!=None:
                tmpsum+=l2.val
                l2=l2.next
            tmp.val=tmpsum%10
            tmpsum //=10
            if l1==None and l2==None and tmpsum==0:
                break
            tmp.next=ListNode(0)
            tmp=tmp.next
        return  ans
