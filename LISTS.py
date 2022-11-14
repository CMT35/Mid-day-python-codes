# LIST

courses = ['History', 'Math', 'Physics', 'Compsci']
# print(len(courses)) - Shows no. of items in a list
courses_2 = ['Art', 'Education']
print(courses[0:2])  # retrieve items from the list

courses.append('art')  # adds item to the list as the last one
courses.insert(0, 'Business')  # adds item: requires index value of the list
courses.extend(courses_2)  # adds each individual item from the second list to the primary list
courses.remove('art')  # remove item from list
# courses.pop(6)           # remove last item from list by default, saves popped item
# courses.reverse() - reverses list from 1st to last
courses.sort()  # sorts in alphabetic order or in ascending order for numbers
print(courses)
print(courses.index('Compsci'))  # returns the index of the item

# example 2
num = [5, 4, 6, 3, 8, 1]
num.sort(reverse=True)  # sorts in reverse order
sorted_num = sorted(num)  # using sorted function when who dont want to alter existing list
print(num)
print(sorted_num)

courses_str = ', '.join(courses)  # Convert the list into a string separated by delimiters
new_list = courses_str.split(', ') # converts back to list format
print(courses_str)
print(new_list)

# Sample example

a = [1, 2, 3]
b = ['Mercedes', 'BMW', 'Audi']

for var1, var2 in zip(a, b):
    print(var1, var2)