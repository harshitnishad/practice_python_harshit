num1=float(input("Enter the first number:"))4.8
num2=float(input("Enter the second number:"))
calc=input("Enter the operator:")
if calc=="+":
    print("The sum of",num1,"&",num2,"is:",num1+num2) 
elif calc=="-":
    print("The substraction of",num1,"&",num2,"is:",num1-num2)
elif calc=="*":
    print("The multiplication of",num1,"&",num2,"is",num1*num2)
elif calc=="/":
    print("The division of",num1,"&",num2,"is:", num1/num2)
else:
    print("invalid")
    