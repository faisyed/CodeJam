class Solution:
    def deleteDuplicates(self, head):
        cur = head
        prev = -1
        prev_node = ListNode(-1)
        while cur:
            if cur.val == prev:
                prev_node.next = cur.next
            else:
                prev = cur.val
                prev_node = cur
            cur = cur.next
        return head