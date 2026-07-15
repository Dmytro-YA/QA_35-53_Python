
numbers = [1,2,3,4,5]
squared = map(lambda x: x**2, numbers)
print(list(squared))
print(squared)

def to_upper(s):
    return s.upper()

statuses = ["active", "inactive", "pending"]
print(list(map(to_upper, statuses)))



