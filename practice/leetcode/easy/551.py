class Solution:
    def checkRecord(self, s):
        a_cnt = 0
        l_cnt = 0
        for ind, val in enumerate(s):
            if val == "A":
                a_cnt += 1
                l_cnt = 0
            elif val == "L":
                l_cnt+=1
            else:
                l_cnt = 0
            if a_cnt>1 or l_cnt>2:
                return False
        return True