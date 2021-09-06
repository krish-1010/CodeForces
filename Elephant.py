n = int(input())

i = 0
count = 0

while i < n:
    if n-i >= 5:
        i += 5
        count += 1
    elif n-i >= 4:
        i += 4
        count += 1
    elif n-i >= 3:
        i += 3
        count += 1
    elif n-i >= 2:
        i += 2
        count += 1
    elif n-i >= 1:
        i += 1
        count += 1
    
print(count)