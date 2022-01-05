class Solution:
    def getDecimalValue(self, head):
        val = head.val
        cur = head.next
        while cur:
            val = val*2 + cur.val
            cur = cur.next
        return val