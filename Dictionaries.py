# Dictionary

student = {'name': 'John', 'age': 25, 'course': ['Math', 'Compsci']}
print(student['course'])  # Access the key
print(student.get('name'))  # Access the key

# Updating dictionary
student.update({'name': 'jane', 'age': 26})  # multiple entries
student['course'] = ['Math', 'Compsci', 'Art']

print(student)

# Deleting
# del student['age']
# age = student.pop('age')

# Retrieving values and keys
# print(student.values())
# print(student.keys())
# print(student.items())

# Looping through a dict
for key, value in student.items():
    print(key, value)

