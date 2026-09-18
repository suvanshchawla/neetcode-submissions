class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max(maxProfit, (prices[sell] - prices[buy]))
            else:
                buy = sell
            sell+=1

        return maxProfit


# Input: prices = [10,1,5,6,7,1]
# We need to find out the max profit possible if we buy and sell the stock once
# We can choose a pointer buy on day 0 and sell on day 1
# if price[l] < price[r] - that means profit, so we updated the maxProfit
# else we update the l price equal to the right because if current selling price is lower than selling price then we can sell on that day