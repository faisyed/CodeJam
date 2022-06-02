# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast =  fast.next.next
        l2, cur = None, slow
        while cur is not None:
            cur.next, l2, cur = l2, cur, cur.next
        rl1,rl2 = head, l2
        while rl2.next is not None:
            rl1.next, rl1 = rl2, rl1.next
            rl2.next, rl2 = rl1, rl2.next
        
            
            