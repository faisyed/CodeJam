class Solution:
    def defangIPaddr(self, address):
        res = ""
        for val in address:
            if val != ".":
                res += val
            else:
                res += "[.]"
        return res
