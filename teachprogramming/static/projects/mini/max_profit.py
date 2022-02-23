from typing import List


def method1(prices):
    return max(
        max(prices[i:]) - price
        for i, price in enumerate(prices)
    )

def method2(prices):
    min_index = prices.index(min(prices))
    max_index = prices.index(max(prices[min_index:]), min_index)
    return prices[max_index] - prices[min_index]

def method3(prices):
    pass
    #todo


def maxProfit(prices: List[int]) -> int:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    Example 1:
    >>> maxProfit([7,1,5,3,6,4])
    5

    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    >>> maxProfit([7,6,4,3,1])
    0

    Explanation: In this case, no transactions are done and the max profit = 0.

    --- some of my tests

    >>> maxProfit([6,5,10,1,2,3,4])
    5
    """
    return method1(prices)



import random, sys
def gen_random_prices(numer_of_random_prices):
    return tuple(
        random.randint(0, sys.maxsize)
        for i in range(numer_of_random_prices)
    )


def _methods_are_the_same(methods=(method1, method2)):
    """
    >>> _methods_are_the_same()
    """
    for i in range(100):
        data = gen_random_prices(2000)
        assert len(set(method(data) for method in methods)) == 1, f"Methods do not produce the same results"


if __name__ == "__main__":
    print("Running timeit benchmark")
    import timeit
    average_time_taken = [
        timeit.timeit(lambda: method(gen_random_prices(2000)), number=3)
        for method in (method1, method2)
    ]
    print(f"{average_time_taken=}")
