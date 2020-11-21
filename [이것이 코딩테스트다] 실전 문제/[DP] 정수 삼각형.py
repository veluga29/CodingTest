# 내 풀이
n = int(input())

# dp 테이블 초기화
dp = [[0] * i for i in range(1, n + 1)]

# 첫 번째 줄 입력값을 기록
dp[0][0] = int(input())

# 두 번째 줄부터 끝까지 다이나믹 프로그래밍 수행 (바텀업)
for i in range(1, n):
    content = list(map(int, input().split()))  # 해당 줄의 입력값 받음
    for j in range(i + 1):
        # 가장 왼쪽 입력값일 때
        if j == 0:
            dp[i][j] = dp[i - 1][j] + content[j]
        # 가장 오른쪽 입력값일 때
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + content[j]
        # 사이 입력값들일 때 왼쪽 위 대각선과 오른쪽 위 대각선의 값들 중 가장 큰 값을 입력값에 더해 갱신
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + content[j]

# 마지막줄에서 가장 큰 값을 반환
print(max(dp[n - 1]))
