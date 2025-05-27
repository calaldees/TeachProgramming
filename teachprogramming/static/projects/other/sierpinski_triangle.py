# https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
# https://stackoverflow.com/questions/1726698/code-golf-sierpinskis-triangle
# https://twitter.com/CompSciFact/status/1785300824379318742
    # f(x,y) = (-(-(~(x | y)))) % 12
# https://github.com/maximecb/Turing-Drawings

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
    while n>1:
        n = n >> 1  # divide by 2
        if x>=n and y>=n:
            return 0
        if x>=n:
            x-=n
        if y>=n:
            y-=n
    return 1


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
