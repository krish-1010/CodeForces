a = input()
b = input()
c = ''

for i in range(len(a)-1,-1,-1):
    c += a[i]

if c == b:
    print('YES')

else:
    print('NO')