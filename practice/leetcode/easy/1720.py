class Solution:
    def decode(self, encoded, first):
        res = list()
        res.append(first)
        for i in range(len(encoded)):
            decode = encoded[i] ^ res[i]
            res.append(decode)
        return res