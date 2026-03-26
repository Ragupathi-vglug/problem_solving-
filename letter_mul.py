#s=input("Enter the String to multiply:")
s="a2b3c9"
result=[]
for i in range(len(s)):
    if s[i].isdigit():
        result.append(s[i-1]*int(s[i]))
print(str(result))



