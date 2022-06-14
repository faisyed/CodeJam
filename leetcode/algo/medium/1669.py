class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cur = list1
        prev = None
        i,j = 0,0
        while cur:
            if i!=a:
                prev = cur
                cur = cur.next
            else:
                break
            i+=1
            j+=1
        prev.next = list2
        while prev.next:
            prev = prev.next
        while cur:
            if j!=b:
                cur = cur.next
                j+=1
            else:
                break
        prev.next = cur.next
        return list1