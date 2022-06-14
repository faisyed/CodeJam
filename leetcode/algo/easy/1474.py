class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = head
        last = head
        while cur:
            i,j = m,n
            while cur and i>0:
                last = cur
                cur = cur.next
                i-=1
            while cur and j>0:
                cur = cur.next
                j-=1
            last.next = cur
        return head