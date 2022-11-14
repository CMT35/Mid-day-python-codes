# FOR LOOP
for cars in list(range(5)):
    print(cars)
print()

# Traversal of string sequence

for letters in 'Python':
    print('Letters in python ', letters)
print()

# Traversal in lists sequence
cars = ['Mercedes', 'BMW', 'Audi', 'Toyota', 'Subaru']
for moti in cars:
    print(moti)
print()

# iterating by sequence index
fruits = ['Apple', 'Bananas', 'Mango', 'Orange']
for index in range(len(fruits)):
    print('Fruits available: ', fruits[index])

# Sample examples 1
# Else executes after loop completes normally
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 5:
        break
    print(f'{num =}')
else:
    print('Not found')


