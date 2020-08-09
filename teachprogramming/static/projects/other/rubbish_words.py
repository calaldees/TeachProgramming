import random

def input_generator(num_words):
    for i in range(num_words):
        yield input(f'word {i} of {num_words}: ')

def rubbish_words(input_generator, min_words=10, max_words=20):
    """
    >>> rubbish_words(('the',), min_words=3, max_words=4)
    'the the the'
    >>> sentence = rubbish_words(('1', '2', '3'), min_words=3, max_words=4)
    >>> assert len(sentence.split(' ')) == 3
    """
    return ' '.join(
        random.choices(
            tuple(input_generator),
            k=random.randrange(min_words, max_words)
        )
    )

if __name__ == '__main__':
    sentence = rubbish_words(
        input_generator=input_generator(num_words=5),
        min_words=10,
        max_words=20,
    )
    print(sentence)
