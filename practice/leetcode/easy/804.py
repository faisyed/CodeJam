class Solution:
    def uniqueMorseRepresentations(self, words):
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        chars = "abcdefghijklmnopqrstuvwxyz"
        hm = {ch: cod for ch, cod in zip(chars, code)}
        st = set()
        for word in words:
            st.add("".join(list(map(hm.get, list(word)))))
        return len(st)
