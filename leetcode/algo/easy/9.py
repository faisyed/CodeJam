class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        tp = x
        while tp!=0:
            n = tp%10
            rev = (rev*10)+n
            tp//=10
        return rev==x