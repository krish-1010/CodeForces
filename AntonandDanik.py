n = int(input())
a = input()

Acount = 0
Dcount = 0

for i in range(n):
    if a[i] == 'A':
        Acount += 1
    elif a[i] == 'D':
        Dcount += 1

if Acount > Dcount:
    print("Anton")

elif Dcount > Acount:
    print("Danik")

elif Acount == Dcount:
    print("Friendship")