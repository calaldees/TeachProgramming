import re

import yaml
def load_data(filename='grammar.yaml'):
    with open(filename, 'rt') as filehandle:
        return yaml.safe_load(filehandle)

data = {
    i: k
    for k,v in load_data().items()
    for i in v
}

known = {*data.keys(), *data.values()}

while sentence := input('> ').lower():
    last_sentence = None
    while sentence != last_sentence:
        print(sentence)
        last_sentence = sentence
        new_sentence = sentence
        for word, replacement in data.items():
            if word in sentence:
                new_sentence = re.sub(f'(^|\s){word}(\s|$)', f' {replacement} ', new_sentence)
        sentence = new_sentence
        #sentence = ' '.join(
        #    data.get(word, word)
        #    for word in sentence.split(' ')
        #)

    print(' '.join(
        word if word in known else f'<{word}>'
        for word in sentence.split(' ')
        if word
    ))
