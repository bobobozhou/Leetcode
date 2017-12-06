def maxProfit(prices):

    # max_profit = 0
    # min_price = float('inf')
    #
    # for price in prices:
    #     min_price = min(min_price, price)
    #     profit = price - min_price
    #     max_profit = max(max_profit, profit)
    #
    # return max_profit

    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return  max_profit


prices = [7, 1, 5, 3, 6, 4]
print (maxProfit(prices))

