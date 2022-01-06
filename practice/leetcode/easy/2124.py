class Solution:
    def checkString(self, s):
        flag_b = False
        for ch in s:
            if ch == "a":
                if flag_b:
                    return False
            else:
                flag_b = True
        return True