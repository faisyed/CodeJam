class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        cnt = 0
        for info in items:
            if ruleKey == "type":
                if info[0] == ruleValue:
                    cnt+=1
            elif ruleKey == "color":
                if info[1] == ruleValue:
                    cnt+=1
            elif ruleKey == "name":
                if info[2] == ruleValue:
                    cnt+=1
        return cnt