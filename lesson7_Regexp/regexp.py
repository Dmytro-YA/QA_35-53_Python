import re

# text = "The test status is passed"
# result = re.search("passed", text)
# print(result)
# print(result.group())

text1 = "passed:test_login"
text2 = "test_login:passed"
print(re.match("passed", text1))
print(re.match("passed", text2))

print(re.fullmatch("passed:test_login", text1))
print(re.fullmatch("passed:test_login1", text1))

print(re.search("c.t", "cat"))
print(re.search("c.t", "cut", ))
print(re.search("c.t", "ct", ))

print(re.search("^Test","Test login page"))
print(re.search("^Test","Login Test page", re.IGNORECASE))

print(re.search("gr[ae]y", "grey",))
print(re.search("gr[ae]y", "gray",))
print(re.search("gr[ae]y", "green",))

print(re.search("[a-z]", "hello"))
print(re.search("[0-9]", "order #42"))
print("=============================================")
print(re.search("[^0-9]","12345a", ))
print(re.search("[^0-9]","12345", ))

print(re.search(r"\d","Order #42"))
print(re.search(r"\w","!!!hello"))
print(re.search(r"\s","no spaces here"))


print(re.search(r"ab*c", "ac"))
print(re.search(r"ab*c", "abc"))
print(re.search(r"ab*c", "abbbc"))

if re.search("passed", text1):
    print("Passed")
else:
    print("Not passed")


