class Solution:
    def findRelativeRanks(self, score):
        srt = sorted(score, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(str(i + 1) for i in range(3, len(score)))
        mp = dict(zip(srt, rank))
        return [mp[i] for i in score]
