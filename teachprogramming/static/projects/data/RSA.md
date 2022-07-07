RSA
===


Consider ...
```python
def coprimes():
    pairs = deque([(2,1), (3,1)])
    while True:
        m, n = p = pairs.popleft()
        yield p
        pairs.append((2*m - n, m))
        pairs.append((2*m + n, m))
        pairs.append((m + 2*n, n))
```
[Raymond Hettinger](https://twitter.com/raymondh/status/1534458117068668929) @raymondh
Cute #Python math algorithm of the day:
This exhaustively lists all combinations of relatively prime positive integers — pairs that don't have a common factor other than one.
To me, this seems like great magic.
Wikipedia attributes the algorithm to various Math Gazette articles (behind a paywall).
My first intuition is that this is essentially the Euclidean GCD algorithm being run in reverse, generating all cases where gcd(m, n) = 1 and m > n.
By covering all possible one-step reductions, it is guaranteed to be exhaustive.