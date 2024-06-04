# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

maxnum = a if a > b else b

# 출력
print(maxnum)