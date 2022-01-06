class Solution:
    def isSumEqual(self, firstWord, secondWord, targetWord):
        s = "abcdefghij"
        mp = {}
        for i in range(10):
            mp[s[i]] = i
        sm1, sm2 = 0, 0
        for ch in firstWord:
            sm1 = (sm1 * 10) + mp[ch]
        for ch in secondWord:
            sm2 = (sm2 * 10) + mp[ch]
        sm = sm1 + sm2
        sm3 = 0
        for ch in targetWord:
            sm3 = (sm3 * 10) + mp[ch]
        return sm == sm3
