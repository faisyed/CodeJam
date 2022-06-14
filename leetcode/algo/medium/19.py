class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l+=1
            cur = cur.next
        cur = head
        i = 1
        if l-n==0:
            return head.next
        while i<(l-n):
            cur = cur.next
            i+=1
        cur.next = cur.next.next
        return head