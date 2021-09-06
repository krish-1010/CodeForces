n = int(input())

a = list(map(int, input().split()))

count = 1
temp = 0
maximum = 0

for i in range(1,n):
    if (a[i-1] <= a[i]):
        count += 1
        temp = count
    else:        
        if (count > maximum):
            maximum = count           
        count = 1

if (n==1):
    print(1)

elif maximum > temp:
    print(maximum)

else:
    print(temp)