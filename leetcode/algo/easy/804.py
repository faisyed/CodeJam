import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lw = string.ascii_lowercase
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mp = {}
        for ch,m in zip(lw,morse):
            mp[ch]=m
        st = set()
        for w in words:
            tp = ""
            for ch in w:
                tp+=mp[ch]
            st.add(tp)
        return len(st)