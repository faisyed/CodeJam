class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mp = {}
        for msg, send in zip(messages, senders):
            l = len(msg.split())
            if send in mp:
                mp[send]+=l
            else:
                mp[send]=l
        mp = dict(sorted(mp.items(), key=lambda item: item[0], reverse=True))
        mp = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))
        return list(mp.items())[0][0]