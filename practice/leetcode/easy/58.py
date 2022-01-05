class Solution:
    def lengthOfLastWord(self, s):
        end = len(s)-1
        while s[end] == " ":
            end -= 1
        cnt = 0
        for i in range(end, -1, -1):
            if s[i] == " ":
                break
            cnt += 1
        return cnt