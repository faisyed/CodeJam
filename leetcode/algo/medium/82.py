class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp = {}
        cur = head
        while cur:
            if cur.val in mp:
                mp[cur.val]+=1
            else:
                mp[cur.val]=1
            cur = cur.next
        res = ListNode(0)
        mv = res
        cur = head
        while cur:
            if mp[cur.val]==1:
                tp = ListNode(cur.val)
                mv.next = tp
                mv = mv.next
            cur = cur.next 
        return res.next