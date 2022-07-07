import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[.!,]?$')
        cnt = 0
        for word in sentence.split():
            if pattern.match(word):
                cnt+=1
        return cnt