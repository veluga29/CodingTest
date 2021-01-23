# 내 풀이
n = int(input())
INF = int(1e9)  # 무한 값으로 10억 설정

# DP 테이블 생성 및 초기화
dp = [0] * 1000001
dp[1] = 0

# 바텀업 다이나믹 프로그래밍 진행
for i in range(2, n + 1):
    d3 = dp[i // 3] if i % 3 == 0 else INF  # 3으로 나누는 경우
    d2 = dp[i // 2] if i % 2 == 0 else INF  # 2로 나누는 경우
    dp[i] = min(d3, d2, dp[i - 1]) + 1  # 세 가지 연산 중 최소 연산 횟수인 경우를 택해, 연산 진행 및 테이블 값 갱신

# 결과 출력
print(dp[n])
