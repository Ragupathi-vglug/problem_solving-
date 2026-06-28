# sol 2
n=int(input("Enter the number :"))
for i in range(n):
    print("*"*i)

# sol 2
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print("")
