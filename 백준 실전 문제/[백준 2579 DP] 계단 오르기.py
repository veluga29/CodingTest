# 내 풀이
n = int(input())  # 계단 수 입력 받기
stairs = [0]  # 시작점 초기화
# 계단 점수 입력 받기
for _ in range(n):
    stairs.append(int(input()))

# 계단이 1개일 경우
if n == 1:
    print(stairs[1])
# 계단이 2개 이상일 경우
else:
    # DP 테이블 생성 및 초기화
    dp = [0] * 301
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    # 바텀업 다이나믹 프로그래밍 수행
    for i in range(3, n + 1):
        # i번째 계단에 두 계단을 밟고 오르는 경우와, 한 계단을 밟고 오르는 경우를 비교해 최대 점수 구하기
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

    # 결과 출력
    print(dp[n])
