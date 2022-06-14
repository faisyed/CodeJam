class Solution:
    def reverse(self,ls):
        cur = ls
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        rev = self.reverse(slow)
        mx = 0
        c1,c2 = head, rev
        while c1:
            mx = max(c1.val+c2.val, mx)
            c1 = c1.next
            c2 = c2.next
        return mx