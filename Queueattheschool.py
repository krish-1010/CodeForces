e, n = map(int, input().split())
q = list(input())

count = 0
i = 0

while i < len(q):
    if q[i] == "B":
        if q[i+1] == "G":
            q[i+1],q[i] = q[i],q[i+1]
            count += 1
            i += 2
            # if q[i+2] != "G":
            #     i += 2
            # else:
            #     i += 1
            if count == n+1:
                break
        i = i + 1

o = ''.join(map(str, q))
print(o)