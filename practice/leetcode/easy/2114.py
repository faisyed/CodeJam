class Solution:
    def mostWordsFound(self, sentences):
        mx = 0
        for sentence in sentences:
            ls = sentence.split(" ")
            cnt = len(ls)
            if cnt>mx:
                mx = cnt
        return mx