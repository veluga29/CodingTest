# 내 풀이
t = int(input())

# dp 테이블 생성 및 초기화
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

# 바텀업 다이나믹 프로그래밍 수행
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

# 각 테스트 케이스 별 결과 출력
for _ in range(t):
    n = int(input())
    print(dp[n])
