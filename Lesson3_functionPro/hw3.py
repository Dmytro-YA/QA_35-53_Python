
def create_profile(name, age=18, city = 'Unknown'):
    return {'name': name, 'age': age, 'city': city}
print(create_profile('Anna'))

#2
def sum_even_numbers(*numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))
print(sum_even_numbers(1,2,3,4,5,6))

#3

def print_pet_info(name, **info):
    if info == {}:
        print(f"Name: {name}\nNo additional information")
    else:
        print(f"Name: {name}\nage: {info['age']}\ncolor: {info['color']}\nbreed: {info['breed']}")

print_pet_info(
"Lucky",
age=4,
color="White",
breed="Spitz"
)
print()
print_pet_info("Lucky")
print()
#4
def merge_lists(*lists):
    if lists == ():
        return []
    return lists[0] + merge_lists(*lists[1:])
print(merge_lists([1,2], [3], [4,5],[]))
print(merge_lists())

#5
def build_message(*words, separator=" "):
    return separator.join(words)
print(build_message("Hello", "World"))
print(build_message("2026","07","15", separator="-"))
