class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profits = []

        for i, x in enumerate(prices):
            p1 = x
            rem = prices[i+1:]

            for y in rem:
                if p1 < y:
                    profits.append(y - p1)

        return max(profits) if profits else 0