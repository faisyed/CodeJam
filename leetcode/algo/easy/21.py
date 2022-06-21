class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        res = head
        c1 = list1
        c2 = list2
        while c1 or c2:
            p1 = c1.val if c1 else 999
            p2 = c2.val if c2 else 999
            if p1<=p2:
                res.next = ListNode(p1)
                res = res.next
                c1 = c1.next if c1 else None
            elif p2<p1:
                res.next = ListNode(p2)
                res = res.next
                c2 = c2.next if c2 else None
        return head.next