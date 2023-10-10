Valid_Operators = ["*", "/", "+", "-", "%", "^2", "^3", "^"]
restart = ""
num1 = float(input("First Number: "))
operator_input = input("Operation" + str(Valid_Operators) + ": ")
num2 = float(input("Second Number: "))
count = 0

if operator_input in Valid_Operators:
    if operator_input == "*":
        print(num1 * num2)

    elif operator_input == "/":
        print(num1 / num2)

    elif operator_input == "+":
        print(num1 + num2)

    elif operator_input == "-":
        print(num1 - num2)

    elif operator_input == "%":
        print(num1 % num2)

    elif operator_input == "^2":
        print(num1 * num1)

    elif operator_input == "^3":
        print(num1 * num1 * num1)

    elif operator_input == "^":
        print(num1 ** num2)

else:


            else:
                print("Invalid Operator")

        restart = input("Would you like to make another calculation?: ")

        if restart.lower() == "no":
            print("Thank you for using this calculator!")
            exit()
        else:
            num_1 = float(input("First Number: "))
            num_operator = input("Operation: ")
            num_2 = float(input("Second Number: "))



