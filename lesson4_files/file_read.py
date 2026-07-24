
with open("users.txt", "w") as file:
    file.write("Alice\nBob\nCharlie")

# read - read the whole file
with open("users.txt", "r") as file:
    content = file.read()
print(content)
print(len(content))

# readline - read one line
with open("users.txt", "r") as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print(line.strip())

print()

with open("users.txt", "r") as file:
    for line in file:
        print(line.strip())