s=input("Enter the word to count vowel:")
result=0
vowels=["a","e","i","o","u"]
for i in s.lower():
    for j in vowels:
        if i==j:
            result+=1
print("The vowel count is :",result)