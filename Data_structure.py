# Tuples
# can't be updated, modified
cars = ('Limo', 'Mercedes', 'Porshe', 'BMW', 'Audi')
print(cars[2])
for gari in cars:
    print(gari)

slicedcars = cars[::-1]
for sg in slicedcars:
    print(sg)

# list
students = ['Samson', 'Chris', 'Emmanuel', 'Owen']
students.append('ted')
# students.pop(0) - remove item from the list using index
# students.remove('Owen') - remove item from the list
students[0], students[2] = students[2], students[0]  # swap the list using the indexes
students[1] = 'Mwangi'  # Edit list element

for stude in students:
    print(stude)

# Dictionaries
users = {'c@test.com': 'Chris', 'E@test.com': 'Emmanuel', 's@test.com': 'Samson', 'o@test.com': 'owen'}

print(users['E@test.com'])

for user in users.values():
    print(user)

for user in users.keys():
    print(user)
