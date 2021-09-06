inp = input()
a = ['a','b','c','d']
count = 5
for i in range(0,len(a)):
    if count == 1:
        break
    for j in range(0,len(inp)):
        if(a[i] == inp[j]):
            count = 1
            break
        else:
            count = 0
if count == 1:
    print("YES")
    
elif count == 0:
    print("NO")