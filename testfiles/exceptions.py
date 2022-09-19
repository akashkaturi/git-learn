import math
def area(radius):
    if radius<=0:
        raise TypeError("Radius cannot be zero or less than zero")
    return math.pi * (radius**2)
try:
    print(area(-10))
except Exception as x:
    print(x)


try:
    print(x)
except NameError:
    print("nope")
# x="hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")
