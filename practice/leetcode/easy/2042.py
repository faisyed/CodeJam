class Solution:
    def areNumbersAscending(self, s):
        prev = -1
        ls = s.split(" ")
        for ch in ls:
            if ch.isdigit():
                num = int(ch)
                if num <= prev:
                    return False
                else:
                    prev = num
        return True