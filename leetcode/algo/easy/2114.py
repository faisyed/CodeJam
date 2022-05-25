class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for sen in sentences:
            mx = max(mx,len(sen.split()))
        return mx