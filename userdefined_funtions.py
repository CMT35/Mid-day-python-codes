def motto():
    print('Hello this is our motto')


motto()


def addition():
    answer = 10 + 20
    print('Your answer is ', answer)


addition()


def sum(x, y, z):
    answer = x + y + z
    print('Hello your answer is ', answer)


sum(2334, 334, 765)


# create a function to calculate the BMI of any person
# use formula = weight divided by height squared
# check and ascertain that if:
# BMI < 24 .............. Underweight
# BMI < 29 .............. normal weight
# BMI < 34 .............. overweight

def bmi(w, h):
    bmi1 = w/pow(h, 2)
    if bmi1 < 24:
        print('Underweight')
    if bmi1 < 29:
        print('Normal weight')
    if bmi1 < 34:
        print('Overweight')
    else:
        print('Obese')


bmi(100, 24)
