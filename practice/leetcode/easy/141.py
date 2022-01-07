class Solution:
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False