class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum_profit = 0

        for i in prices:
            minimum = min(minimum, i)
            maximum_profit = max(maximum_profit, i - minimum)
        return maximum_profit