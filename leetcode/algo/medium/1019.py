class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ar = []
        cur = head
        while cur:
            ar.append(cur.val)
            cur = cur.next
        st = [(0,ar[0])]
        res = [0]*len(ar)
        for ind in range(1,len(ar)):
            if st and ar[ind]<=st[-1][1]:
                st.append((ind,ar[ind]))
            else:
                while st and st[-1][1]<ar[ind]:
                    res[st[-1][0]] = ar[ind]
                    st.pop()
                st.append((ind,ar[ind]))
        return res