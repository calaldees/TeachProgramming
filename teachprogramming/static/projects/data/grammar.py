import re
from itertools import chain

import yaml
def load_data(filename='grammar.yaml'):
    with open(filename, 'rt') as filehandle:
        return yaml.safe_load(filehandle)

data = load_data()

while sentence := input('> ').lower():
    last_sentence = None
    while sentence != last_sentence:
        print(sentence)
        last_sentence = sentence
        for replacement, words in data.items():
            for word in words:
                _sentence = sentence
                sentence = re.sub(f'(^|\s){word}(\s|$)', f' {replacement} ', sentence)
                if sentence != _sentence:
                    print(sentence)

    known = tuple(chain(data.keys(), chain.from_iterable(data.values())))
    print(' '.join(
        word if word in known else f'<{word}>'
        for word in sentence.split(' ')
        if word
    ))
