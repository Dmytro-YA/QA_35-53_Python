


def print_string_reverse(s):
    if s is None or s == '' or s == ' ':
        return "Wrong string"
    return s[::-1]

s = input()
print(print_string_reverse(s))


#2

def is_isr_phone_number(phone):
    if phone is None or phone == '' or phone == ' ':
        return None
    if phone.isdigit() and len(phone) == 10 and phone.startswith('0'):
        return True
    return False
s1 = input()
print(is_isr_phone_number(s1))

#3

def print_substring_reverse(s, start, finish):
    if s is None or s == '' or s == ' ' or start < 0 or finish > len(s) or start > finish:
        return "Wrong args"
    part = s[start:finish+1]
    part_reverse = part[::-1]
    return s[0:start] + part_reverse + s[finish+1:len(s)]
s = input()
start = int(input())
finish = int(input())
print(print_substring_reverse(s, start, finish))

#4

def get_words_reverse(s):
    " ".join(s.split()[::-1])
    return " ".join(s.split()[::-1])


s = input()
print(get_words_reverse(s))

#5

def print_words_reverse_in_column():
    for i in s.split():
        print(i[::-1])

s = input()
print_words_reverse_in_column()


