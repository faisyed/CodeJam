class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for item in items:
            if ruleKey=='type' and ruleValue==item[0]:
                cnt+=1
            elif ruleKey=='color' and ruleValue==item[1]:
                cnt+=1
            elif ruleKey=='name' and ruleValue==item[2]:
                cnt+=1
        return cnt
                