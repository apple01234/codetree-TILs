a, b = map(int, input().split())
sum_val = 0

for i in range(a, b or b, a):
    if i % 5 == 0:
        sum_val += i

print(sum_val)