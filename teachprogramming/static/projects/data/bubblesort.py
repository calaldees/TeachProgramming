
def bubblesort(data):
    """
    >>> bubblesort(['a', 'b', 'c', 'd'])
    ['a', 'b', 'c', 'd']
    >>> bubblesort(['b', 'd', 'c', 'a'])
    ['a', 'b', 'c', 'd']
    """
    items_have_changed = True
    while items_have_changed:
        items_have_changed = False
        #print(data)
        for i in range(len(data)-1):
            a = data[i]
            b = data[i+1]
            #print(f'comparing {i}:{a} with {i+1}:{b}')
            if a > b:
                #print(f'swapping {i}:{a} with {i+1}:{b} -> {i}:{b} and {i+1}:{a}')
                data[i] = b
                data[i+1] = a
                items_have_changed = True
    #print('no items have changed places - the list is now sorted')
    return data

if __name__ == '__main__':
    print(bubblesort(['b', 'd', 'c', 'a']))
