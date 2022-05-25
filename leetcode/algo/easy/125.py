class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for ch in s:
            if ch.isalnum():
                res+=ch
        return res == res[::-1]