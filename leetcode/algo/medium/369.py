# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, llist):
        prev, cur = None, llist
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def plusOne(self, head: ListNode) -> ListNode:
        l = self.reverse(head)
        cur = l
        car = 1
        res = ListNode(0)
        tp = res
        while cur:
            v = cur.val
            sm = cur.val+car
            tp.next = ListNode(sm%10)
            tp = tp.next
            car = sm//10
            cur = cur.next
        if car>0:
            tp.next = ListNode(1)
            tp = tp.next
        return self.reverse(res.next)