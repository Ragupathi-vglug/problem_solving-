s=input("Enter the String :")
# s="abca"
for i in s:
    if s.count(i)==1:
        print("The non repeated value is :",i)
        break
# result=[]
# for i in s:
#     if i==s[i]:
#         result.append(s[i])
# print("The not repeated value is :",result[0])