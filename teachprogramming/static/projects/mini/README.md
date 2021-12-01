Mini Algorithum Projects
========================


In a row
--------
```python
def in_a_row(data):
    """
    >>> in_a_row('')
    0
    >>> in_a_row('a')
    1
    >>> in_a_row('b')
    1
    >>> in_a_row('ab')
    1
    >>> in_a_row('aa')
    2
    >>> in_a_row('aab')
    2
    >>> in_a_row('abb')
    2
    >>> in_a_row('aabbcc')
    2
    >>> in_a_row('aabbbcc')
    3
    """
    return
```


Fibbonach
---------
```python
def fib(v):
    """
    >>> next_fib(0):
    1
    >>> next_fib(1):
    1
    """
```



https://www.olympiad.org.uk/papers/2009/bio/round_one.html

A digit word is a word where, after possibly removing some letters, you are left with one of the single digits: 
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT or NINE.
For example:
• BOUNCE and ANNOUNCE are digit words, since they contain the digit ONE.
• ENCODE is not a digit word, even though it contains an O, N and E, since they are not in order

Write a program which reads in a single upper-case word (with at most fifteen letters) 
and determines if it is a digit word. 
If the word is not a digit word you should output the word NO. If the word is a digit 

word you should output the digit it contains, as a number.
You will not be given any words which contain more than one digit


is_anagram(a, b) {

}


Single digets only
123 ok
1223 not ok
321 ok
3321 not ok
67 ok
66 not ok

tower(3)
```
  #
 ###
#####
```

tower(4)
```
   #
  ###
 #####
#######
```


is_prime



```python
def fizzbuzz(i):
    """
    * [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz#Programming_interviews) [_](https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/)
        * > Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
        * In under 5min (Pro) - in under 10min (A Grade)
        * [Tom Scott commentary and solution](https://www.youtube.com/watch?v=QPZ0pIK_wsc)

    >>> tuple(map(fizzbuzz, range(100)))
    ('fizzbuzz', 1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz', 'fizz', 22, 23, 'fizz', 'buzz', 26, 'fizz', 28, 29, 'fizzbuzz', 31, 32, 'fizz', 34, 'buzz', 'fizz', 37, 38, 'fizz', 'buzz', 41, 'fizz', 43, 44, 'fizzbuzz', 46, 47, 'fizz', 49, 'buzz', 'fizz', 52, 53, 'fizz', 'buzz', 56, 'fizz', 58, 59, 'fizzbuzz', 61, 62, 'fizz', 64, 'buzz', 'fizz', 67, 68, 'fizz', 'buzz', 71, 'fizz', 73, 74, 'fizzbuzz', 76, 77, 'fizz', 79, 'buzz', 'fizz', 82, 83, 'fizz', 'buzz', 86, 'fizz', 88, 89, 'fizzbuzz', 91, 92, 'fizz', 94, 'buzz', 'fizz', 97, 98, 'fizz')
    """
    r = ''
    if i % 3 == 0:
        r += 'fizz'
    if i % 5 == 0:
        r += 'buzz'
    if not r:
        r = i
    return r
```



```python
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
    """
    return method2(prices)


if __name__ == "__main__":
    print("Running timeit benchmark")
    import timeit, random, sys
    def gen_random_prices(numer_of_random_prices):
        return list(
            random.randint(0, sys.maxsize)
            for i in range(numer_of_random_prices)
        )
    average_time_taken = [
        timeit.timeit(lambda: method(gen_random_prices(2000)), number=3)
        for method in (method1, method2)
    ]
    print(f"{average_time_taken=}")

```
