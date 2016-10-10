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

def product_of_other_ints(lst):

    products = []

    for i in range(len(lst)):
        product = 1
        new_lst = lst[:i] + lst[i + 1:]
        for num in new_lst:
            product *= num
        products.append(product)

    return products

def my_function(arg):
    # write the body of your function here
    product_before = [None] * len(arg)
    product_so_far = 1
    
    for i in range(len(arg)):
        product_before[i] = product_so_far
        product_so_far *= arg[i]
        
    print product_before

def highest_product(lst_of_ints):

    if len(lst_of_ints) < 3:
        return "Exception! Input list must have at least three values."

    highest = max (lst_of_ints[0], lst_of_ints[1])
    lowest = min(lst_of_ints[0], lst_of_ints[1])

    highest_prod_2 = lst_of_ints[0] * lst_of_ints[1]
    lowest_prod_2 = lst_of_ints[0] * lst_of_ints[1]

    highest_prod_3 = lst_of_ints[0] * lst_of_ints[1] * lst_of_ints[2]

    for item in lst_of_ints[2:]:
        highest_prod_3 = max(highest_prod_3, item * highest_prod_2, item * lowest_prod_2)
        highest_prod_2 = max(highest_prod_2, item * highest)

def merge_ranges(lst):

    lst = sorted(lst)

    merged = [lst[0]]

    for item in lst[1:]:
        to_check = merged[-1]
        if item[0] == to_check[1] + 1 or item[0] == to_check[1]:
            new = (to_check[0], item[1])
            merged[-1] = new
        elif item[0] < to_check[1]:
            if item[1] < to_check[1]:
                continue
            else:
                new = (to_check[0], item[1])
                merged[-1] = new
        else:
            merged.append(item)

    return merged






