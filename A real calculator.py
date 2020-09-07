
# REMEMBER:
# # user input is always string
# so eval(12 - 10) is eval (string) but the output is an integer
# eval evaluates about everything.. even text... so be careful

import re

print("This is a killer calculator")
print("Type 'quit' to exit\n")

previous = 0  # previous holds the result of the previously calculated equation
run = True


def PerformMath():
    global run  # run is creating outside the function, to access the function, use global
    global previous
    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))  #

    if equation == 'quit':  # if user writes quit, run = False, so no PerformMath()
        print("goodbye. Human")
        run = False
    else:  # otherwise:
        equation = re.sub('[A-Za-z,.:()" "]', '', equation)  # remove all alphabets, commas in equation

        if previous == 0:  # check again if previous = 0
            previous = eval(equation)  # evaluate equation which is whatever is inputted by user i.e string
                                        # the output of eval is not a string but an integer
        else:  # if it is not equal to 0, if there are evaluations made
            print("I'm going to run this thru eval", str(previous) + equation)  # print it and eval
            previous = eval(str(previous) + equation)

        print(previous)


while run:
    PerformMath()

# understand the code better:
equation = input("Enter Equation: ")
previous = eval(equation)
print(eval(equation))
print(type(equation))
print(previous)
print(type(previous))
