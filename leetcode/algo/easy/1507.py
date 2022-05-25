class Solution:
    def reformatDate(self, date: str) -> str:
        mp = {"Jan" :"01", "Feb" :"02", "Mar" :"03", "Apr" :"04", "May" :"05", "Jun" :"06", "Jul" :"07", "Aug" :"08", "Sep" :"09", "Oct" :"10", "Nov" :"11", "Dec" :"12"}
        ls = date.split()
        day = ls[0][:-2] if len(ls[0])==4 else "0"+ls[0][:-2]
        res = ls[2]+"-"+mp[ls[1]]+"-"+day
        return res