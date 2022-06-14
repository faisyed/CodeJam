class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = ListNode(0)
        cur = head
        mv = res
        while cur:
            if cur.val!=val:
                tp = ListNode(cur.val)
                mv.next = tp
                mv = mv.next
            cur = cur.next
        return res.next