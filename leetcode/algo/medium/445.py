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
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rl1 = self.reverse(l1)
        rl2 = self.reverse(l2)
        car = 0
        res = ListNode(0)
        cur = res
        while rl1 or rl2:
            v1 = rl1.val if rl1 else 0
            v2 = rl2.val if rl2 else 0
            sm = v1+v2+car
            cur.next = ListNode(sm%10)
            car = sm//10
            cur = cur.next
            rl1 = rl1.next if rl1 else None
            rl2 = rl2.next if rl2 else None
        if car>0:
            cur.next = ListNode(car)
            cur = cur.next
        return self.reverse(res.next)