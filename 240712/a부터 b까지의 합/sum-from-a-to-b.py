sum_val = 0
a, b = map(int, input().split())

for i in range(a, b+1):
    sum_val += a+b
print(sum_val // 2)