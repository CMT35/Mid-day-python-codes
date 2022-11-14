# LOOPS
# While loop
counter = 0
while counter <= 5:
    print(counter)
    counter += 1

countertwo = 90
while countertwo >= 85:
    print(countertwo)
    countertwo -= 1

counter_three = 20
while counter_three <= 50:
    if counter_three % 2 == 1:
        print(counter_three)
    counter_three += 1

# For in loop
number = range(3, 20, 2)
for i in number:
    print(i)

marks = range(40, 101, 10)
for mark in marks:
    if mark <= 40:
        print('E')
    if mark <= 50:
        print('D')
    if mark <= 60:
        print('C')
    if mark <= 70:
        print('B')
    else:
        print('A')
