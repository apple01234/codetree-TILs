# 변수 선언, 입력
n = input()
arr = n.split()

a = int(arr[0])
b = int(arr[1])

# 출력
if a > b:
	print(a * b)
else:
	print(b / a)