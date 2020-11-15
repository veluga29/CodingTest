# 내 풀이
n, m = map(int, input().split())
value = [int(input()) for _ in range(n)]

dp = [0] * (m + 1)

for i in range(1, m + 1):
    # 보유한 화폐 하나로 구성할 수 있는 금액인 경우
    if i in value:
        dp[i] = 1
        continue

    for v in value:
        # (i - v) 금액의 화폐 구성이 가능하고 아직 i 금액의 화폐 구성을 안해본 경우
        if dp[i - v] != 0 and dp[i] == 0:
            dp[i] = dp[i - v] + 1
        # (i - v) 금액의 화폐 구성이 가능하고 이미 i 금액의 화폐 구성 시도가 있었던 경우
        if dp[i - v] != 0 and dp[i] != 0:
            dp[i] = min(dp[i], dp[i - v] + 1)  # 최소 화폐 개수 체크

if dp[m]:
    print(dp[m])
else:
    print(-1)

