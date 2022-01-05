class Solution:
    def finalPrices(self, prices):
        st = list()
        for ind, val in enumerate(prices):
            while st and prices[st[-1]]>=val:
                prices[st.pop()]-=val
            st.append(ind)
        return prices