n = input()
a = input()
count = 0


for i in range(len(a)-1):
    if a[i+1] == a[i]:
        count += 1

print(count)
