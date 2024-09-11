sum_val = 0
cnt = 0

for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        cnt += 1
        sum_val += n

num_val = sum_val / cnt  
print(sum_val, end = " ")
print(f"{num_val:.1f}")