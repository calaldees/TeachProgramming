Max Profit
==========

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
(could be used at a coding interview)

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


Hints
-----

<details>

1. You need a method to get the `max` value in an array.
2. You need to maybe be able to slide an array e.g. [1,2,3,4,5] -> get the last 3 as -> [3,4,5]

A simple solution is 2 or 3 lines using streams

</details>


Advanced
--------

<details>

* The next interview question would be how could you optimise this?
* Generate a a random array of `int`s that is 10,000 items long anf run your solution on it.
    * Can you use some kind of timeit logger or performance profiler to get an idea of how long it takes to run?
* Optimise it! Make it 100's of times faster.
    * (I've got ideas, but I need to put them in my solutions ... have a think)
    * Optimisation questions are a VERY common next question in any coding interview situations
        * See fizzbuzz drag racing
        * See isPrime drag racing

</details>