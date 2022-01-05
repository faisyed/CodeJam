class Solution:
    def findTheDifference(self, s, t):
        val = 0
        for ch in s:
            val^=ord(ch)
        for ch in t:
            val^=ord(ch)
        return chr(val)