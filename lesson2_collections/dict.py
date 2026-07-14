books = {
    'Harry Potter and ......':'J.K. Rowling',
    'To Kill a Mockingbird':'Harper Lee',
    'The Great Gatsby': 'F. Scott Fitzgerald'
}
books1 = {
    'Harry Potter and ......',
    'To Kill a Mockingbird',
    'The Great Gatsby'
}
print(books)
print(books1)
data = [1,22,3]
print(isinstance(data,list))

value = 10
print(type(value))
print(isinstance(value,(int, float)))

team_ages = {
    'Alex':23,
    'Bob':25,
    'Tom':22,
    'Jane':21,
    'Kate':20
}
print(team_ages.keys())
print(type(team_ages.keys()))
print(team_ages.values())

team_names = [ 'Alex', 'Bob', 'Tom', 'Jane', 'Kate']
team_numbers = [23, 25, 22, 21, 20]
team_ages = dict(zip(team_names, team_numbers))
print(team_ages)