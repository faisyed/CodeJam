class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        for i, a in enumerate(prices):
            while st and prices[st[-1]]>=a:
                prices[st.pop()]-=a
            st.append(i)
        return prices