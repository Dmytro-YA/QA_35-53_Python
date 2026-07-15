
def double(x):
    return x * 2
print(double(5))

x = lambda y: y * 2 if y > 0 else y*10
print(x(-5))

add = lambda x,y: x+y
print(add(1,2))

is_even = lambda x: x % 2 == 0
print(is_even(10))
print(is_even(11))