num=int(input("Enter the Number of rows you want :"))
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for s in range(2*i-1):
        print("*",end="")
    print()