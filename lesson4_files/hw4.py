import csv
import json
import os
from pathlib import Path


#1
def save_shopping_list(items):
    with open("shopping.txt", "w") as file:
        for item in items:
            file.write(item + "\n")

items = ["Milk", "Bread", "Apples", "Coffee"]
save_shopping_list(items)

with open("shopping.txt", "r") as file:
    print(file.read())


#2

def read_students(filename):
    with open("student.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Student: {row['name']}({row['age']})")

read_students("student.csv")


#3

def save_profile(name, age, city):
    profile = {"name": name, "age": age, "city": city}
    with open("profile.json", "w") as file1:
        json.dump(profile, file1, indent=4)

save_profile("Maria", 30, "Haifa")

#4

def create_reports_folder():
    reports_dir = Path("reports1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir / "result.txt"
    with open(result_file, "w") as file:
        file.write("Report generated successfully.")
create_reports_folder()

