# WHILE LOOP

count = 0

while count <= 9:
    print('The count is ', count)
    count += 1

print('Good bye')

# problem 2
var = 0
while var < 5:
    print(var, ' is less than 5')
    var += 1
else:
    print(var, ' is not less than five')

# Problem 3
# Else statement executes when loop completes normally
num = 0
while num < 5:
    print(f'{num = }')
    num += 1
else:
    print('Loop has completed successfully')

print()

# scenario 2
number = 0
while number < 8:
    if number == 3:
        break

    number += 1
    print(f'{number = }')
else:
    print('Wagwan')

# Problem 4
# Print length of each string in the list
my_cars = ['Mercedes', 'Audi', 'Range rover', 'Jaguar']
index = 0
while index < len(my_cars):
    element = my_cars[index]
    print(len(element))
    index += 1

# scenario 2 we will take a list of numbers, and iterate over each number using while loop, and in the body of while
# loop, we will check if the number is even or odd.

my_num = [1, 2, 3, 4, 5, 6, 7]
index = 0
while index < len(my_num):
    if my_num[index] % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
    index += 1



