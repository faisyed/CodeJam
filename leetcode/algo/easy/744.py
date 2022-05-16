class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target<letters[0]:
            return letters[0]
        l, h = 0, len(letters)-1
        res = letters[0]
        while l<=h:
            mid = (l+h)//2
            if letters[mid]>target:
                res = letters[mid]
                h = mid-1
            else:
                l = mid+1
        return res