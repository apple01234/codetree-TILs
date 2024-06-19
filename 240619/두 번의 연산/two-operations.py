# 변수 선언 및 입력
a = int(input())

if a % 2 == 1:
    a += 3
    
if a % 3 == 0:
    a //= 3

print(a)