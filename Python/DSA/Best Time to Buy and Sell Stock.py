class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute force approach - O(n^2): Pick an index and beyond that index check for all possible value which maximise the negative difference, if the difference is positive, return 0
        min_price = float('inf')
        max_profit = 0
        for i, num in enumerate(prices):
            min_price = min(num,min_price)
            val = num-min_price
            max_profit = max(val,max_profit)
        return max_profit
        #Optimised approach - O(n): Keep track of minimum price so far and calculate profit at each step. Update max profit if current profit is greater than max profit.