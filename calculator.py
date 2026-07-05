while True:
    print("==================================")
    print("         COS202 CALCULATOR")
    print("==================================")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, _,*, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
       print("Answer =", num1 + num2)

    elif operator == "_":
         print("Answer =", num1 - num2)

    elif operator == "*":
         print("Answer =", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by zero.")
        else:
            print("Answer =", num1 / num2)

    elif operator == "%":
        print("Answer =", num1 % num2)

    elif operator == "^":
        print("Answer =", num1 ** num2)

    else:
        print("Invalid operator!")

    choice = input("\nDo you want to calculate again? (yes/no): ")

    if choice.lower() == "no":
        print("Calculator turned OFF.")
        break
                 

                
