numbers = (1, 2, 3, 4, 5)
print(numbers)
my_tuple = ([1, 2, 3], [4, 5, 6], ['a', 'b', 'c'])

first_element = my_tuple[0]
print(first_element)
nested_tuple = (1,2, (3,4,5))

my_tuple = (1,2,3,4,5)
print( 3 in my_tuple)
print( 10 in my_tuple)
for el in my_tuple:
    print(el)

i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1
print()

my_tuple = (1,2,3,4,5)
lenght_of_tuple = len(my_tuple)
print(lenght_of_tuple)

sum_of_elements = sum(my_tuple)
print(sum_of_elements)
max_element = max(my_tuple)
print(max_element)
min_element = min(my_tuple)
print(min_element)

my_tuple1 = ()
print(len(my_tuple1))
print(sum(my_tuple1))
# print(max(my_tuple1))
# print(min(my_tuple1))

print('===============================')

original_tuple = (3,1,5,9,7,1,5,6,4,2,0)
sorted_tuple = tuple(sorted(original_tuple))
print('original',original_tuple)
print('sorted',sorted_tuple)

subtuple = original_tuple[3:7]
print(subtuple)

print('===============================')
my_tuple = list(original_tuple)
my_string = str(original_tuple)
my_string1 = ''.join(map(str, original_tuple))
print(my_string1)
print(my_tuple)
print(my_string)

print('===============================')
my_tuple = (1,2,3,4,5)
print(my_tuple)
my_list = list(my_tuple)
my_list[2] = 10
updated_tuple = tuple(my_list)
print(updated_tuple)