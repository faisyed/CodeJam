class Solution:
    def reverse(self, ls):
        cur, prev = ls,None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
    
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos,neg = ListNode(0),ListNode(0)
        m1,m2 = pos,neg
        cur = head
        while cur:
            if cur.val>=0:
                tp = ListNode(cur.val)
                m1.next = tp
                m1 = m1.next
            else:
                tp = ListNode(cur.val)
                m2.next = tp
                m2 = m2.next
            cur = cur.next
        pos = pos.next
        neg = neg.next
        if neg is None:
            return pos
        if pos is None:
            return self.reverse(neg)
        rev = self.reverse(neg)
        mv = rev
        while mv.next:
            mv = mv.next
        mv.next = pos
        return rev