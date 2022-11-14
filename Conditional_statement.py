# this is an if statement
# age = int(input('enter your age: '))

# if age >= 20:
   # print('Welcome to to the party')
#else:
  #  print('Sorry , you cant attend this party')

# Project 1 simple interest calculator

# principle = float(input('Enter your principle\n'))
# rate = float(input('Enter the rate\n'))
# time = float(input('Enter the time\n'))

# simple_interest = (principle + rate + time) / 100

# if simple_interest <= 1000:
  #  print('The loan is affordable')
#elif simple_interest <= 1000:
#    print('The loan is expensive')
# else:
  #  print('The loan is a scam')

# Project 2 Grading system

user_input = input('Welcome to Emobilis, what is your name: ')

Math_grade = int(input(f'{user_input} kindly share with us your math score\n'))

if Math_grade <= 40:
    print(f'You have a attained a math grade of {Math_grade}: Fail')
elif Math_grade > 40 <= 75:
    print(f'You have a attained a math grade of {Math_grade}: Pass')
elif Math_grade > 75 <= 100:
    print(f'You have a attained a math grade of {Math_grade}: Excellent')
else:
    print('Invalid number')
