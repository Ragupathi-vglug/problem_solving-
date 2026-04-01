expenses = [
    ("food", 120),
    ("transport", 50),
    ("food", 80),
    ("entertainment", 200),
    ("transport", 30),
    ("food", 100)
]
res=[]
for i in expenses:
    for j in range(len(i)):
        if str(i[j]) not in res:
            res.append(i[j])
print(res)