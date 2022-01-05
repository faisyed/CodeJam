class Solution:
    def flipAndInvertImage(self, image):
        return [[ val^1 for val in row[::-1]] for row in image]