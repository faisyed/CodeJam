class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ls = sentence.split()
        res = []
        vow = "aeiouAEIOU"
        for i, word in enumerate(ls):
            if word[0] in vow:
                res.append(word+"ma"+"a"*(i+1))
            else:
                res.append(word[1:]+word[0]+"ma"+"a"*(i+1))
        return " ".join(res)