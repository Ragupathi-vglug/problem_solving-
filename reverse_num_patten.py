a=int(input("Enter the number: "))
for i in range(a+1):
    p=a
    for i in range(i):
        print(p,end="")
        p-=1
    print("")
