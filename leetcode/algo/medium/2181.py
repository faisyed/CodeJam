class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        last = None
        res = ListNode(0)
        mv = res
        sm = 0
        while cur:
            if last is not None:
                if cur.val!=0:
                    sm+=cur.val
                else:
                    tp = ListNode(sm)
                    last = cur
                    mv.next = tp
                    mv = mv.next
                    sm = 0
                cur = cur.next
            else:
                if cur.val == 0:
                    last = cur
                cur = cur.next
        return res.next