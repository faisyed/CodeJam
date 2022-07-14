class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        st,en = s.split(":")
        st_r,st_c = st[0],int(st[1])
        en_r,en_c = en[0],int(en[1])
        prev_st = st_c
        res = []
        while st_r<=en_r and st_c<=en_c:
            res.append(st_r+str(st_c))
            st_c+=1
            if st_c>9 or st_c>en_c:
                st_c = prev_st
                st_r = chr(ord(st_r)+1)
        return res