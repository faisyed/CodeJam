# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        st = [slow.val]
        while slow.next:
            slow = slow.next
            st.append(slow.val)
        cur = head
        while len(st)>0:
            if cur.val != st.pop():
                return False
            cur = cur.next
        return True