n=int(input("Enter how many rows :"))
for i in range(n,0,-1):
      print("*"*i)

# sol 2
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")