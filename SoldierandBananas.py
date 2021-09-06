x, m, n = map(int, input().split())

Tc = 0

for i in range(1,n+1):
    Tc += x*i 

B = Tc-m
if B < 0:
    B = 0
print(B)