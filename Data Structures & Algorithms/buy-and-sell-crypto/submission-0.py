class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case prices empty or < 2 
        # Algorithm - track buy and sell date in pointers day 0 and day 1
        # track max profit. If the value at sell day is less than the value at buy day
        # Essentially we are trying to find an interval in an array where the start and end are maximally different yielding the most profit

        if len(prices) < 2:
            return 0
        
        max_profit = 0
        buy, sell = (0, 1)

        while sell < len(prices):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        
        return max_profit


        