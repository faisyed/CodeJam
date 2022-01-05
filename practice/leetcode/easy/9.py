class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        rev = 0
        tp = x
        while x!=0:
            n = x%10
            rev = (rev*10)+n
            x//=10
        if rev==tp:
            return True
        return False