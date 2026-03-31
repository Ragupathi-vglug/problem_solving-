s=input("Enter the string :")
revstr=""
for i in s:
    revstr=i+revstr
if revstr==s:
    print("The given atring is a palindrome ")
else:
    print("The given string is not a palindrome")
