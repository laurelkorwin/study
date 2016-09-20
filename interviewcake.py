stock_prices_yesterday = [10, 12, 7, 5, 2, 11, 8, 9]

def get_max_profit(stock_lst):

    if len(stock_lst) <= 1:
        return 0

    first_half = stock_lst[:len(stock_lst) / 2]
    second_half = stock_lst[len(stock_lst) / 2:]

    first_half_best = get_max_profit(first_half)
    second_half_best = get_max_profit(second_half)

    cross = max(second_half) - min(first_half)

    maximum = max(first_half_best, second_half_best, cross)

    return max(first_half_best, second_half_best, cross)

def get_max_profit2(stock_lst):

    min_price = stock_lst[0]

    max_profit = 0

    for stock in stock_lst:
        min_price = min(min_price, stock)
        current_profit = stock - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit
