n, k = input().split()

n, k= int(n),int(k)

a = list(map(int, input().split()))

kth = a[k-1]

counter = 0

for i in range(n):
    if (a[i] >= kth and a[i] != 0):
        counter += 1
    else:
        break
           
print(counter)