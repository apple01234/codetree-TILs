a, b = map(int, input().split())

while(a <= b+2):
    if(a % 2 == 0):
        a += 2
        print(a, end = " ")