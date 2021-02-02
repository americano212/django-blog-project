A = input("Enter list A numbers :").split()
B = input("Enter list B numbers :").split()
result =[]

for i in A :
    if i not in B :
        result.append(int(i))
        result.sort()

for i in B :
    if i not in A :
        result.append(int(i))
        result.sort()

print(result)
