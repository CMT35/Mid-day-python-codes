# TUPLES
tuple_1 = ('History', 'Math', 'Physics')
tuple_2 = tuple_1

# Cant be manipulated

# SETS
courses = {'History', 'Math', 'Physics', 'Compsci', 'Math'}
# Removes duplicates
print(courses)
# membership test
print('Math' in courses)

# To show which items appear in 2 list
cars = {'Mercedes', 'BMW', 'Audi'}
cars_jdm = {'Jeep', 'Toyota', 'Mercedes'}

print(cars.intersection(cars_jdm))
print(cars.difference(cars_jdm))  # items that dont appear twice
print(cars.union(cars_jdm))  # Join 2 sets


