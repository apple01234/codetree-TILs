# 변수 선언 및 입력
n = int(input())
cnt2, cnt3, cnt12 = 0, 0, 0

# 각 날짜마다 확인합니다.
for i in range(1, n + 1):
    # 주기가 가장 긴 12일부터 확인합니다.
    if i % 12 == 0:
        cnt12 += 1
    # 12일 주기에 들어오지 않는다면, 3일 주기에 들어오는지 확인합니다.
    elif i % 3 == 0:
        cnt3 += 1
    # 3일 주기에도 들어오지 않는다면, 2일 주기에 들어오는지 확인합니다.
    elif i % 2 == 0:
        cnt2 += 1

print(cnt2, cnt3, cnt12)