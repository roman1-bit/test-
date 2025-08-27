from math import ceil

def square(a):
    if isinstance(a, int) or (isinstance(a, float) and a.is_integer()):
        side = int(a)
    else:
        side = ceil(a)
    return side * side

print(square(5.1))
