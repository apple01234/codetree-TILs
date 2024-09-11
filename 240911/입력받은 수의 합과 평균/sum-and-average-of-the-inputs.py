n = int(input())
sum_val = 0

for i in range(n):
   num = int(input())
   sum_val += num

num_val = sum_val / n
print(sum_val, end = " ")
print(f"{num_val:.1f}")