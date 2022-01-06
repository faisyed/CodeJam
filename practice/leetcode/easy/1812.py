class Solution:
    def squareIsWhite(self, coordinates):
        mpalpha = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        mpdig = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8}
        return False if mpalpha[coordinates[0]] % 2 == mpdig[coordinates[1]] % 2 else True
