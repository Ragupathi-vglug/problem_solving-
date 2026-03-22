nums=[1,2,2,3,4,5,7,7,6,5,4,8]
res=[]
for i in nums:
    if i not in res:
        res.append(i)
print(res)
print(list(set(nums)))

