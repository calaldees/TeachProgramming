### DNA

Human DNA 3 Billion pairs
1 byte = 4 pairs (A-G,C-T) (2 bits per item. 4 items in 1 byte)

* https://medium.com/precision-medicine/how-big-is-the-human-genome-e90caa3409b0
    * 200GB (off the sequencer)
    * 125MB (variant of a reference genome) (diff from reference)
    * 700MB (perfect world)

1. Find manually by looking at the data
    1. kneedle in a haystack
2. Implement a `findindex` function ourselfs with a for loop
    * See [Coding Challenge #156: Peeking inside Pi](https://www.youtube.com/watch?v=MEdpRYyjz_0) for some examples
    * ```python
        def find_index(data, target):
            """
            We would normally not do this as it's built in `'abcd'.find('bc')`
            But it's a good learning exercise

            >>> find_index('abcdefghijklmnopqrstuvwxyz', 'abc')
            0
            >>> find_index('abcdefghijklmnopqrstuvwxyz', 'ijk')
            8
            >>> find_index('abcdefghijklmnopqrstuvwxyz', 'and')
            False
            """
            j = 0
            for i in range(len(data)):
                if data[i] == target[j]:
                    j += 1
                    if j >= len(target):
                        return i - j + 1
                else:
                    j = 0
            return False
      ```
    * Explain the problem of partial matching - code will become more complex
        * `AC[AG]`
        * `.{2,3}`
3. Show the power of regex

[regex101.com](https://regex101.com/)
```python
import random
import re
random.seed(0)
dna = ''.join(random.choice(('A', 'G', 'C', 'T')) for x in range(10000))
re.search(r'AC[AG].GT.{8,10}AAA', dna)
re.search(r'AC[AG].GT[AT]{5,6}AAA', dna)
```