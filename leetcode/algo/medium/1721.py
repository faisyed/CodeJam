class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0
        cur = head
        while cur:
            l+=1
            cur = cur.next
        p1 = head
        i = 1
        while i<k:
            p1 = p1.next
            i+=1
        p2 = head
        i=1
        while i<=l-k:
            p2 = p2.next
            i+=1
        p1.val,p2.val = p2.val,p1.val
        return head