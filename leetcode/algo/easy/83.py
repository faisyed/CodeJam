# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, cur = head, head.next
        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev.next = cur
                prev = cur
            cur = cur.next
        return head