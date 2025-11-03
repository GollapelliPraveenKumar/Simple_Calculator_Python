
"""
Simple Calculator using Python
This is a Beginner Friendly Python Project
Covered Topics :
1. Arithmatical Operators
2. Conditional Statements
3. Built-in Functions

"""


print("Simple_Calculator")
print("Select Operation : ")
print("1.Addition(+)")
print("2.Subtract(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Modulus(%)")
print("6.Power(**)")

choice = input("Enter Choice(1/2/3/4/5/6 or +-*/%**): ")

num1 = float(input("Enter First Number : "))
num2 = float(input("Enter Second Number : "))

if choice == "1" or choice == "+":
    result = num1 + num2
    print(f"Result : {num1} + {num2} = {result}")

elif choice == "2" or choice == "-":
    result = num1 - num2
    print(f"Result : {num1} - {num2} = {result}")

elif choice == "3" or choice == "*":
    result = num1 * num2
    print(f"Result : {num1} * {num2} = {result}")

elif choice == "4" or choice == "/":
    if num2 == 0 :
        print("Error | Division by zero is not allowed")
    
    else :
        result = num1 / num2
        print(f"Result : {num1} / {num2} = {result}")

elif choice == "5" or choice == "%" :
    result = num1 % num2
    print(f"Result : {num1} % {num2} = {result}")

elif choice == "6" or choice == "**" :
    result = num1 ** num2
    print(f"Result : {num1} ** int{num2} = {result}")

else :
    print("Invalid Input | Please select a valid Operation.")