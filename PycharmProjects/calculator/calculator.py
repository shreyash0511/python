print()
print("welcome to the calculator")
print("put in the first number to calculate ")
num1 = int(input())
op = input("choose an operator ")
print("next number")
num2 = int(input())

if op == "*":
    print("the answer is ",num1 * num2)
elif op == "+":
    print("the answer is ",num1 + num2)
elif op == "-":
    print("the answer is ",num1 - num2)
elif op == "/":
    print("the answer is ",num1 / num2)
else:
    print("not able to make")