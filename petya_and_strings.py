a = input().lower()
b = input().lower()

max_index = len(a)-1
i,j = 0,0

while a[i] == b[j] and i != max_index:
    i += 1
    j += 1

if a[i] > b[j]:
    print(1)

elif a[i] < b[j]:
    print(-1)

else:
    print(0)





