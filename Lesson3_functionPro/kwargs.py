
def print_config(**kwargs):
    print(type(kwargs))
    print(kwargs)

print(print_config(name="Alice", age=25, city="New York"))
print_config()

def create_user(**data):
    return data
user = create_user(name="Alice", age=25, city="New York")
print(user)

def example(a,b=10, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


example(1, 2, 3,4, name="Alice", age=25, city="New York")