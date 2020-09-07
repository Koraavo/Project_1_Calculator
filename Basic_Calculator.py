# creating as code to power up the index number

def raise_to_power(index_num, power_num):
    result = 1
    for power in range(power_num):
        result = result * index_num
    return result


print (raise_to_power(2, 3))

print("-----------------------------------------------------------------------")

print("Here's a Basic Calculator")

Word = "Y"
question = ""
count = 0
your_answer_is = True
question = input("Do you want to try the basic calculator, Y or N: ")
if question.islower():
    question = question.upper()
while question == Word:
    def calc():
        Num1 = float(input("Enter the first number: "))
        Operator = input("Please enter Operator: ")
        Num2 = float(input("Enter the second number: "))
        if Operator == "+":
            print(Num1 + Num2)
        elif Operator == "-":
            print(Num1 - Num2)
        elif Operator == "*":
            print(Num1 * Num2)
        elif Operator == "/":
            print(Num1 / Num2)
        else:
            print("Invalid Operator")
    calc()
    if count == 0:
        question = input("Do you want more?, Y or N: ")
        if question.islower():
            question = question.upper()
else:
    your_answer_is = not True

# if not true

if not your_answer_is:
    # print(bool(your_answer_is))
    print("your answer was No")

print("--------------------------------------------------------")






