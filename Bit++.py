n = int(input())

x = 0

for i in range(n):
    a = input() #string

    if (a[1] == '+'):
        x += 1
    elif (a[1] == '-'):
        x -= 1

print(x)



# ++X, X++ a[0]
# --X, X--