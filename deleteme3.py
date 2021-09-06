n = int(input())
s = ''
for i in range(n):
    a = input()
    s+=a

print(s)

str1 = "hello world I'm a software"
print(str1.split())
print(str1.split("l"))

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

temp = [0, 22.5, 40,100]
F_temps = list(map(fahrenheit, temp))
print(F_temps)