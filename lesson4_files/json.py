import json

#dumps() - Python -> JSON str
#loads() - JSON -> Python


#dump() - Python -> JSON file
#load() - JSON -> Python file

user = {"username": "Alice", "age": 25, "is_admin" : True}
json_string = json.dumps(user)
print(json_string)
print(type(json_string))

json_python = json.loads(json_string)
print(json_python)
print(type(json_python))
print(json_python["username"])


test_config = {
    "base_url" : "https://api.example.com",
    "timeout" : 10,
    "retries" : 3,
    "1":True
}
print("--------------------------------------------")
with open("config.json", "w") as file:
    json.dump(test_config, file, indent = 2, ensure_ascii=False)

with open("config.json", "r") as file:
    config = json.load(file)
    print(config)
    print(config["base_url"])