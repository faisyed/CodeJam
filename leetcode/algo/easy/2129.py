class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ls = title.split()
        for ind,w in enumerate(ls):
            if len(w)<=2:
                ls[ind] = w.lower()
            else:
                ls[ind] = w.capitalize()
        return " ".join(ls)