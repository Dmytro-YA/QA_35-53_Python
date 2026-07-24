def get_list_element(item, index):
    try:
        return item[index]
    except IndexError as e:
        return "IndexError:"

numbers = [1,2,3,4,5]
print(get_list_element(numbers, 10))
print(get_list_element(numbers, -1))

def get_user_data(user, key):
    try:
        return user[key]
    except KeyError as e:
        return "Key is not exist"

user = {"name": "Alice", "age": 25}
print(get_user_data(user, "name"))
print(get_user_data(user, "salary"))


print("--------------------------------------------")

def calculate_average(first_value, second_value):
    try:
        return (float(first_value) + float(second_value)) / 2
    except ValueError:
        return "Value is not float"
    except TypeError:
        return "Value is not float invalid"

print(calculate_average("10","20"))
print(calculate_average("hello", "20"))
print(calculate_average(None, "20"))

#
# def read_number():
#     try:
#         user = int(input("Enter number: "))
#     except ValueError:
#         print( "Value is not int")
#     else:
#         print("Number is correct")
#     finally:
#         print("Programm is finished")
# read_number()


def validate_age(age):
    if age < 0:
        raise ValueError("Age must be positive")
    if age > 120:
        raise ValueError("Age must be less than 120")
    print("ok")
# validate_age(10)
# validate_age(-1)
# validate_age(150)
try:
    validate_age(25)
except ValueError as e:
    print(e)

try:
    print(validate_age(-25))
except ValueError as e:
    print(e)

print("**********************************************")

ages = [10,20,30,40,50, -5, 150]
for age in ages:
    try:
        validate_age(age)
    except ValueError as e:
        print(e)



