
#1
def print_list_reverse(lst):
    print(lst[::-1])

print_list_reverse([1,2,3,4,5])

#2
def is_valid_point(point):
    print(len(point))
    print(type(point))
    if point == () or point == None:
        return None
    if ((type(point) == tuple and len(point) == 2)
            and (isinstance(point[0], (int, float)) and isinstance(point[1], (int, float)))):
        return True
    else:
        return False


print(is_valid_point((1,2)))


#3
def print_sublist_reverse(lst, start, finish):
    reversed_sub = lst[start:finish+1][::-1]
    print(lst[0:start] + reversed_sub + lst[finish+1:len(lst)])

print_sublist_reverse([10, 20, 30, 40, 50, 60],1, 3)

#4

def get_students_by_grade(students):
    if students == None or students == [] or type(students) != dict:
        return {}
    result = {}
    for name, mark in students.items():

        if mark not in result:
            result[mark] = []
        if mark in result:
            result[mark].append(name)
    return result

print(get_students_by_grade({"Alice": 90, "Bob": 85, "Diana": 90, "Charlie":85}))
