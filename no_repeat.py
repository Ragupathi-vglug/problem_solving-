# s=input("Enter the String :")
s="abca"
# for i in s:
#     if s.count(i)==1:
#         print("The non repeated value is :",i)
#         break
result=[]
# for i in range(len(s)):
#     if not(s[i]==s[i+1] or s[i]==s[i-1]):
#         result.append(s[i])
#         break
for i in s:
    if i is not s:
        result.append(i)
        break
if result is not None:
    print("The not repeated value is :",result[0])
else:
    print("There is no repeating value Found!")