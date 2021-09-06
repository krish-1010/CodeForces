n = int(input())


for i in range(n):
    
    a = input()
    b = a[1:-1]
    c = str(len(b))

    if len(a) > 10:
        d = a[0]+c+a[-1]

    else:
        d = a 
    

    print(d)