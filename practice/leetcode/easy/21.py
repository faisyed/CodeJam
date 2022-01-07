class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode(0)
        cur = head
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val <= p2.val:
                tp = ListNode(p1.val)
                cur.next = tp
                p1 = p1.next
            elif p2.val < p1.val:
                tp = ListNode(p2.val)
                cur.next = tp
                p2 = p2.next
            cur = cur.next
        cur.next = p1 or p2
        return head.next
