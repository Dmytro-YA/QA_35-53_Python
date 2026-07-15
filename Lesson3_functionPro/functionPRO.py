

def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)
# res1 = greet()
# print(res1)

def create_user(name, role = "user"):
    return {"name": name, "role": role}
print(create_user("Alice"))
print(create_user("Bob", "admin"))
print()

def calculate_discount(price, discount=10):
    return price - price * discount / 100
print(calculate_discount(100))
print(calculate_discount(100, 22))

def add_test_result(name, results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_test_result("Alice"))
print(add_test_result("Bob"))

def create_user1(username, email, role):
    return f"{username} ({email}) has role {role}"

print(create_user1("Alice", "alice_admin@gmail.com", "'admin'"))
print(create_user1(role = 'admin', username= 'Alice', email = 'alice_admin@gmail.com'))












