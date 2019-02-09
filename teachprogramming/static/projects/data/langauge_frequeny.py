from collections import defaultdict
import re
from itertools import groupby
from functools import partial
from pprint import pprint


def _load_file_data(filehandle):
    r"""
    >>> _load_file_data([
    ...     '# https://en.wikipedia.org/wiki/Letter_frequency',
    ...     'Letter \tEnglish \tFrench',
    ...     'a \t8.16% \t*7.636%',
    ... ])
    {'English': {'a': 0.0816}, 'French': {'a': 0.07636}}
    """
    language = defaultdict(dict)
    language_index_lookup = []
    for line in filehandle:
        if line.startswith('#'):
            continue
        line_split = tuple(i.strip() for i in line.split('\t'))
        if not language_index_lookup:
            language_index_lookup = line_split
            continue
        for index, col in enumerate(line_split[1:]):
            language[language_index_lookup[index+1]][line[0]] = float(re.search('[\d.]+', col).group())/float(100)
    return dict(language)
def load_file_data(filename):
    with open(filename, 'rt', encoding='utf-8') as filehandle:
        return _load_file_data(filehandle)


def _detect_language_by_letter_frequency(language_letter_frequency_data, text):
    text = text.lower()
    text = re.sub('\W', '', text)  # Remove all non-word characters
    text = re.sub('\d', '', text)  # Remove all digits (because digits are apparently word characters?)
    text_letter_frequency = {letter: len(tuple(letter_list))/len(text) for letter, letter_list in groupby(sorted(text))}
    return {
        language: sum({
            letter: abs(letter_frequency - text_letter_frequency.get(letter, 0))
            for letter, letter_frequency in language_letter_frequency.items()
        }.values())
        for language, language_letter_frequency in language_letter_frequency_data.items()
    }
def detect_language_by_letter_frequency(language_letter_frequency_data, text):
    pprint(text)
    langauge_frequencys = _detect_language_by_letter_frequency(language_letter_frequency_data, text)
    pprint(langauge_frequencys)
    return sorted(langauge_frequencys.items(), key=lambda i: i[1])[0][0]

language_letter_frequency_data = load_file_data('langauge_frequeny.txt')

detect_language = partial(detect_language_by_letter_frequency, language_letter_frequency_data)

text = """
Letter frequencies, like word frequencies, tend to vary, both by writer and by subject. One cannot write an essay about x-rays without using frequent Xs, and the essay will have an idiosyncratic letter frequency if the essay is about the use of x-rays to treat zebras in Qatar. Different authors have habits which can be reflected in their use of letters.
"""

text2 = """
L’émulateur peut faire fonctionner quelques jeux, mais très moyennement dans la plupart des cas. L’objectif de l’auteur est d’atteindre un niveau de qualité qui permettra à quiconque de jouer son jeu favori PlayStation 2 sur son PC.
"""


pprint(detect_language(text))
pprint(detect_language(text2))
