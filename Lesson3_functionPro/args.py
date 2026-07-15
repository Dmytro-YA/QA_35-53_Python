
def total(*args):
    print(type(args), args)
    return sum(args)
print(total(1,2,3,4,5))
print(total(10,20))
print(total(10,20,30,40,50))
print(total())
print()

def print_scores(student, *scores):
    print(f"Student {student}")
    print("scores:", scores)

print_scores("Alice", 90, 85, 75)
print_scores("Bob", 95)

print()

def check_status_codes(*codes):
    for code in codes:
        assert code == 200

print(check_status_codes(200, 200, 200))
print(check_status_codes(200, 200, 200, 400))


