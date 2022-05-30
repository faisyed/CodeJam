# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        car = 0
        res = ListNode(0)
        cur = res
        while l1 is not None or l2 is not None:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            sm = v1+v2+car
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            cur.next = ListNode(sm%10)
            cur = cur.next
            car = sm//10
        if car>0:
            cur.next = ListNode(car)
        return res.next