n = int(input())
no = 0
max = 0
for i in range(n):
    out, inp  = map(int, input().split())
    no -= out
    no += inp
    if no > max:
        max = no

print(max)
    