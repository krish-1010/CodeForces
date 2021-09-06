n = int(input())
a = list(map(int, input().split()))
a.append(-10)

count = 1
max = 0

for i in range(n):
    if a[i] <= a[i+1]:
        count+=1
    else:
        if count > max:
            max = count
        count = 1

print(a)