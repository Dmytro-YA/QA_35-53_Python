


empty_list = []
mixed_list = [1, 'apple', 2.5, 'banana']
fruits = ['orange', 'peach', 'lemon']

print(fruits[0])

fruits[1]='blueberry'
print(fruits)
print('-------------------')
list1=['orange', 'peach']
list2=['shampoo', 'soap']
combo_list = list1 + list2
print(combo_list)
print('-------------------')
fruits = ['orange', 'peach', 'lemon']
first,second, third = fruits
print(first)
print(second)
print(third)
for item in fruits:
    print(item, end=' ')

print('=====================================')
correct_answers=['apple', 'banana', 'orange']
user_answers=['apple', 'banana', 'peach', 'orange']
if user_answers == correct_answers:
    print('All answers are Correct!')
else:
    print('Some answers are incorrect!')

print(len(user_answers))
print(max(user_answers))
print(min(user_answers))
print('===================================')

res = sorted(user_answers)
print(res)
print(user_answers)
print(sorted(user_answers, reverse=True))
word = 'python'
result = ''.join(sorted(word))
print(result)

print('===================================')

names = ['Alexander', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names, key=len))
names.sort()
print(names)