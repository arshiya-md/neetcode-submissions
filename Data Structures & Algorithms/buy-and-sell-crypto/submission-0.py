class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        past_lowest = prices[0]
        for curr_day in range(1, len(prices)):
            profit = prices[curr_day] - past_lowest
            max_profit = max(max_profit, profit)
            past_lowest = min(past_lowest, prices[curr_day])

        return max_profit


        