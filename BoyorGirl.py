a = input()

i = 0

while i <= len(a)-1:    
    if i == len(a)-1:
        break
    
    elif a[i] in a[i+1:]:
        a = a[:i]+a[i+1:]
        i = i - 1
 
    i += 1        
 
if len(a) % 2 == 0:
    print("CHAT WITH HER!")
 
else:
    print("IGNORE HIM!")