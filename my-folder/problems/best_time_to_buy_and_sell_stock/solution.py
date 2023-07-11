class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n^2)
        # profit = 0
        # for i in range(0, len(prices)):
        #     for m in range(i+1, len(prices)):
        #         profit = max(profit, prices[m] - prices[i])
        # return profit

        #O(n)
        buy = 10000
        sell = 0
        profit = 0

        for i in prices:
            if i<= buy:
                buy = i
                #found a cheaper buy price so sell is after buy, reinitialize sell price to 0
                sell = 0
            elif i>=sell:
                sell = i
            profit = max(sell-buy, profit)
        return profit