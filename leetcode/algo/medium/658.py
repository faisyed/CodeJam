class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr, key= lambda v:abs(v-x))
        arr = arr[:k]
        return sorted(arr)