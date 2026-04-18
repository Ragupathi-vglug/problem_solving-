f_num=int(input("Enter the first number :"))
l_num=int(input("Enter the last number :"))
print("+\n-\nx\n/\n%")
sym=input("Enter the operation :")
if sym=="+":
    print(f"The addition of {f_num} and {l_num} is {f_num+l_num}")
elif sym=="-":
    print(f"The Subtraction of {f_num} and {l_num} is {f_num-l_num}")
elif sym.lower() =="x":
    print(f"The Multiplication of {f_num} and {l_num} is {f_num*l_num}")
elif sym == "/":
    print(f"The Division of {f_num} and {l_num} is {f_num/l_num}")
elif sym=="%":
    print(f"The Modulus of {f_num} and {l_num} is {f_num%l_num}")
else:
    print("The given operation is not found ")

