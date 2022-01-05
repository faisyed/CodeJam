class Solution:
    def mostCommonWord(self, paragraph, banned):
        s = paragraph.lower()
        res = ""
        for ch in s:
            if ch.isalpha():
                res+=ch
            else:
                res+=" "
        words = res.split()
        mp = defaultdict(int)
        for word in words:
            if word not in banned:
                mp[word]+=1
        return max(mp, key=mp.get)