while True:
    Operator = input("Enter Operator(+,-,*,/) : ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if Operator == "+":
        print(num1 + num2)
    elif Operator == "-":
        print(num1 - num2)
    elif Operator == "*":
        print(num1 * num2)
    elif Operator == "/":
        if num2 == 0:
            print("we cannot divide by zero")
        else:
             print(num1 / num2)
    else:
        print(" Operator not found")
    choice = input("Do you want to continue (y/n)? ")
    if choice == "y":
        continue
    else:
        print("process ended")
        break
