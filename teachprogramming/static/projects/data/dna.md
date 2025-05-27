DNA
===

The field of BioInformatics.


Human Genome Size
-----------------

The human genome is 3.2 billion pairs (gigabases)
1 byte = 4 pairs (A-G,C-T) (2 bits per item. 4 items in 1 byte)

> Genome size varies between species and doesn't necessarily reflect the size of the organism. For example, the genome of the Japanese flower Paris japonica is about 50 times larger than the human genome. The marbled lungfish has the largest recorded genome of any eukaryote, with one haploid copy of its genome containing 132.8 billion base pairs.

* https://medium.com/precision-medicine/how-big-is-the-human-genome-e90caa3409b0
    * 200GB (off the sequencer)
    * 125MB (variant of a [reference genome](https://en.wikipedia.org/wiki/Reference_genome)) (diff from reference)
    * 700MB (perfect world)

<details>
<summary>How big?<summary>

* 1 Billion is 1000 Million
    * 1,000,000 * 1000 = 1,000,000,000 (9  zeros)
* Circumference of the earth (equator) = 40,075 Killometers
    * 1 kilometers is 1000 meters
    * 1 meter is 100 centimeters
    * 40,075 * 1000 * 100 = 4,007,500,000 = 4 Billion centimeters
* If each AGCT was written on a 1cm square of paper (3.2 billion centimeters) - your DNA would wrap around 80% (3.2/4) of the planet
</details>


Activities
----------

### 1. Find manually by looking at the data

Printout `dna1` and `dna2` generated from the code below.
```python
# regex101.com
import random
import re
random.seed(0)
def gen_dna(size=6000):
    return ''.join(random.choice(('A','G','C','T')) for x in range(size))
dna1 = gen_dna()
dna2 = gen_dna()
print(dna1)
print()
print()
print(dna2)

defect = r'GTAC[AC].TT'
print(re.search(defect, dna1))
print(re.search(defect, dna2))
```

* Which one has the genetic defect `GTAC[AC].TT`
    * Needle in a haystack.


### 2. Implement a `findindex` function ourselves with a for loop
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

### 3. Show the power of regex

[regex101.com](https://regex101.com/)

```python
DEFECT = r'GTAC[AC].TT'
re.search(DEFECT, dna1)
re.search(DEFECT, dna2)

#re.search(r'AC[AG].GT.{8,10}AAA', dna1)
#re.search(r'AC[AG].GT[AT]{5,6}AAA', dna1)
```

* A slightly fake problem. Genetic defects normally reside in the same place in the DNA chain. So this activity seeds a misconception.
* However! Searching for a sequence is very much the job of an aligner - so the skill/technique still has valid use in the field of bioinfomatics.

### 4 View a real human genome

* https://en.wikipedia.org/wiki/Genome_browser
* https://en.wikipedia.org/wiki/UCSC_Genome_Browser

* Browse the human genome
    * [National Center for Biotechnology Information (ncbi)](https://www.ncbi.nlm.nih.gov/gdv/browser/genome/?chr=17&from=73060031&to=73970032&id=GCF_000001405.40)
    * [UCSC Genome Browser (web)](https://genome.ucsc.edu/)
    * [ensembl](http://www.ensembl.org/Homo_sapiens/Location/View?r=17:73514968-73515099;db=core)

### 5. Explain an 'Aligner' for sequencing DNA




More BioInformatics
------------------

* [Rosalind](http://rosalind.info/) - learning BioInformatics and programming through problem solving
    * [Transcribing DNA into RNA](http://rosalind.info/problems/rna/)
    * [Semiglobal Alignment](http://rosalind.info/problems/smgb/)
* [Sequencing your DNA with a USB dongle and open source code](https://stackoverflow.blog/2021/12/24/sequencing-your-dna-with-a-usb-dongle-and-open-source-code/)
* [Download Complete Genomes](https://hgdownload.soe.ucsc.edu/downloads.html)
