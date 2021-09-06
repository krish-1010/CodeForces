l1 = []
for i in range(5):
    a = list(map(int, input().split()))
    l1.append(a)
    for j in range(5):
        if l1[i][j] == 1:
            o = abs(2-i)+abs(2-j)
print(o)