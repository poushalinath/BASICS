# get the numbers from user
number1 = int(input(">"))
number2 = int(input(">"))
# tell the user about the options
print("press 1 for addition press 2 for subtraction press 3 for multification press 4 for divide")
operator = input(">")
print("your answer is:")
if operator == "1":
    print(number1+number2)
elif operator == "2":
    print(number1-number2)
elif operator == "3":
    print(number1*number2)
elif operator == "4":
    print(number1/number2)
else:
    print("the input is invalid")