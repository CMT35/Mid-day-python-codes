marks = []
total = 0

print('Enter marks for 5 subjects: ')

# Ask the user to input marks for 5 subjects
for i in range(5):
    marks.append(i)
    marks.append(input())
for i in range(5):
    total = total + marks[i]

avg = total / 5

if avg <= 40:
    print(f'You have a attained an average of {avg}: Fail')
elif avg > 40 <= 75:
    print(f'You have a attained an average of {avg}: Pass')
elif avg > 75 <= 100:
    print(f'You have a attained an average {avg}: Excellent')
else:
    print('Invalid number')
