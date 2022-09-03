def cal(a, b, op):
    if op=="+":
        result = a + b
        print(result)
        return result
    elif op=="-":
        return print(result=a-b)
    elif op=="*":
        return print(result=a*b)
    elif op=="/":
        return print(result=a/b)
    else:
        return print("Invalid operator!")
def cu():
    cont=input("Do you want to continue? if yes type 'y': ").lower()
    while cont=="y":
        result=num1
        operator = input("Choose the operator\n +\n -\n *\n /\n")
        num2 = int(input("Enter the second number: "))
        cal(a=num1, b=num2, op=operator)
num1=int(input("Enter first number: "))
cu()

