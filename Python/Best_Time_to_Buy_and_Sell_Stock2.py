def maxProfit(prices):

    # max_profit = 0
    #
    # for i in range(len(prices)-1):
    #
    #     max_profit += max(prices[i + 1] - prices[i], 0)
    #
    # return max_profit

    max_profit = 0

    for i in range(len(prices) - 1):

        max_profit += max(prices[i + 1] - prices[i], 0)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print (maxProfit(prices))
