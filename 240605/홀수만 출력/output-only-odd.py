num = input()
arr = num.split()
a = int(arr[0])
b = int(arr[1])

for i in range(a, b+1, a + 1):
    print(i, end = " ")