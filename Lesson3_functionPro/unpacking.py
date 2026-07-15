
def login(username, password):
    print(username, password)

data = ["admin", "123456"]
login(data[0], data[1])
login(*data)

user = {
    "username": "admin", "password": "123456"

}
login(**user)

# user = {"username": "admin", "password": "123456", "role": "admin"}
# login(**user)

