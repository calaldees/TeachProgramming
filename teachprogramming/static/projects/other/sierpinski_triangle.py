# https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
# https://stackoverflow.com/questions/1726698/code-golf-sierpinskis-triangle


def isPowerOfTwo(x):
    return (x & (x - 1)) == 0

def _triangle(n, x, y):
    """
    >>> _triangle(1, 0, 0)
    1
    >>> _triangle(2, 0, 0)
    1
    >>> _triangle(2, 1, 0)
    1
    >>> _triangle(2, 0, 1)
    1
    >>> _triangle(2, 1, 1)
    0
    """
    if n==1:
        return 1
    _half_n = n/2
    if x>=_half_n and y>=_half_n:
        return 0
    return _triangle(_half_n, x if x<_half_n else x-_half_n, y if y<_half_n else y-_half_n)


def triangle(n):
    """
    >>> print(triangle(1))
    #
    >>> print(triangle(2))
    ##
    # 
    >>> print(triangle(4))
    ####
    # # 
    ##  
    #   
    >>> print(triangle(8))
    ########
    # # # # 
    ##  ##  
    #   #   
    ####    
    # #     
    ##      
    #       
    >>> print(triangle(16))
    ################
    # # # # # # # # 
    ##  ##  ##  ##  
    #   #   #   #   
    ####    ####    
    # #     # #     
    ##      ##      
    #       #       
    ########        
    # # # #         
    ##  ##          
    #   #           
    ####            
    # #             
    ##              
    #               
    """
    assert isPowerOfTwo(n)
    return '\n'.join(
        ''.join('#' if _triangle(n,x,y) else ' ' for x in range(n))
        for y in range(n)
    )


if __name__ == "__main__":
    print(triangle(1))
    print()
    print(triangle(2))
    print()
    print(triangle(4))
    print()
    print(triangle(8))
    print()
    print(triangle(16))
    print()
    print(triangle(32))
    print()
    print(triangle(64))