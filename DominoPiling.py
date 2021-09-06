a, b = input().split()
a, b = int(a), int(b)

AreaofBoard = a*b

AreaofDomino = 2

if (AreaofBoard % 2 != 0):

    NDomino = (AreaofBoard-1)/2

else:
    NDomino = AreaofBoard/2

print(int(NDomino))