"""
Question paper (A-level): Paper 1 June 2017 [AQA-75171-QP-JUN17.PDF](https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2017/june/AQA-75171-QP-JUN17.PDF) Q7 14 Marks
2h30min = 100marks 150min  = 9min

One method that can be used to compress text data is run length encoding 
(RLE). When RLE is used the compressed data can be represented as a set of 
character/frequency pairs. When the same character appears in consecutive 
locations in the original text it is replaced in the compressed text by a single 
instance of the character followed by a number indicating the number of 
consecutive instances of that character. Single instances of a character are 
represented by the character followed by the number 1.
Figure 9 and Figure 10 show examples of how text would be compressed using 
this method.
Figure 9
Original text: AAARRRRGGGHH
Compressed text: A 3 R 4 G 3 H 2
Figure 10
Original text: CUTLASSES
Compressed text: C 1 U 1 T 1 L 1 A 1 S 2 E 1 S 1 
What you need to do
Task 1
Write a program that will perform the compression process described above. 
The program should display a suitable prompt asking the user to input the text to 
compress and then output the compressed text.
Task 2
Test the program works by entering the text AAARRRRGGGHH.
Task 3
Test the program works by entering the text A.
"""

# Not a brilliant solution - but works .. took 4min

def compress(t):
    """
    >>> compress('AAARRRRGGGHH')
    'A 3 R 4 G 3 H 2'

    >>> compress('CUTLASSES')
    'C 1 U 1 T 1 L 1 A 1 S 2 E 1 S 1'
    """
    out = []
    _l = t[0]
    _count = 0
    for l in t:
        if l == _l:
            _count += 1
        else:
            out.append((_l,_count))
            _count = 1
            _l = l
    out.append((_l,_count))
    return ' '.join(f'{l} {c}' for l, c in out)

if __name__ == "__main__":
    import doctest
    doctest.testmod()