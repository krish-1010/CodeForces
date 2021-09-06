a = input()

count = 0
cc = 0

for i in a:
    if i.isupper():
        count += 1
    else:
        cc += 1

if count > cc:
    a = a.upper()

elif(count <= cc):
    a = a.lower()

print(a)