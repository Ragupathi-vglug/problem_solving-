def factorial(x):
    if x==1:
        return 1
    else:
        fact=x*factorial(x-1)
        return fact
n=int(input("Enter the number :"))
print(f"The factorial of {n} is {factorial(n)}") 
