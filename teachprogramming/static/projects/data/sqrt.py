# Estimate

def square_root(number):
    x = 1
    for i in range(0, 10):
        x = (x+number/x)/2
    return x

number = float(input("Type a number:"))
sqrt = square_root(number)
print(sqrt)
