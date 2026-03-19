s=input("Enter the string :")
# s="aabbc"
result=[]
for i in s:
    if s.count(i)==1:
       result.append(i) 
if len(result)==0:
    print(None)
else:
    print(result[0])