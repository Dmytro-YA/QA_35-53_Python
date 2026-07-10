# age = 25
# name = 'Ivan'
#
# said = "She said \"Hello\""
# print(said)
#
# my_string = ("""This is multyline string.
# we have wrapped text to the next line""")
# print(my_string)
#
# raw_string = r"This is raw string\fg\dfddfg\er"
# print(raw_string)
#
# print(type(raw_string))
#
# s = 5
# print(type(s))
# s3 = True
# print(type(s3))
#
# s1 = 'zeleno'
# s2 = 'glasko'
# print(s1 + s2)
#
# words = ['zeleno', 'glasko', 'kuku']
# qw = " ` ".join(words)
# print(qw)
#
# print(words[0]*5)
#
# print(words[0][0])

s1 = "Vasya Pupkin"
s2 = "Vasya"
if s2 in s1:
    print("Yes")
else:
    print("No")

st='a'
if st == 'a' or st == 'b' or st == 'c' or st == 'd':
    print("Yes")

if st in 'abcde':
    print("Yes")
#****************************************************************

ln = len("Zelenoglazka")
print(ln)

st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])
st = 'Python'
print(st[0:3])
print(st[3:5])

my_string = "Hello, world!"
print(my_string[::2])
reversed_string = my_string[::-1]
print(reversed_string)


raw = " Today is a good day "
raw = raw.strip().replace(' ','*')
print(raw)

date_str = "09,07,2026"
date_list = date_str.split(',')
print(f"Год: {date_list[2]}, Месяц: {date_list[1]}, День: {date_list[0]}")


