# 내 풀이
n = int(input())

# 자리수마다 가장 뒤에 오는 숫자 0 ~ 9를 고려하는 DP 테이블 생성
dp = [[0] * 10 for _ in range(101)]
# DP 테이블 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 바텀업 다이나믹 프로그래밍 수행
for i in range(2, 101):
    # 0과 9에 대해 점화식 수행
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    # 1 ~ 8까지의 점화식 수행
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

# 결과 출력
print(sum(dp[n]) % int(1e9))
