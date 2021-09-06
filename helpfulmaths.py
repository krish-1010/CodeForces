a = input()
c = ''
l = []
for i in a:
    if i != '+':
        c += i

c = sorted(c)

for i in c:
    l.append(i)
    l.append('+')

l.pop()
c = ''.join(l)
print(c)


