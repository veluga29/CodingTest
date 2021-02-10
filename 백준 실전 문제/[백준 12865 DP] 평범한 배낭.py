# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 고려할 변수가 2개일 때, 2차원 DP 테이블을 만들어 접근한다는 생각을 가져야겠다.
n, k = map(int, input().split())
items = [(0, 0)]

# 물품 정보 입력 받기
for i in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# 2차원 DP 테이블 생성 및 초기화
dp = [[0] * (k + 1) for _ in range(n + 1)]

# 냅색 알고리즘 수행
for i in range(1, n + 1):
    # 물품 중 하나를 선택
    w = items[i][0]
    v = items[i][1]
    # 1 ~ k까지의 무게에 대해 다이나믹 프로그래밍 진행
    for j in range(1, k + 1):
        # 선택한 물품의 무게가 가방 허용 무게를 넘어갈 경우
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 선택한 물품의 무게가 가방 허용 무게 안쪽일 경우
        else:
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[n][k])
