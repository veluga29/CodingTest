# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 경우의 수를 잘 나누지 못해 문제 푸는 것이 어려웠다. 아이디어 기억하자.

n = int(input())
wine = [0]  # 인덱스를 맞추기 위해 0 추가

# 와인 정보 입력 받기
for _ in range(n):
    wine.append(int(input()))

# DP 테이블 생성 및 초기화
dp = [0] * 10001
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1):
    # 3가지 경우를 고려
    # 1. i 번째 와인을 마시지 않는 경우
    # 2. i 번째 외인을 마시는 경우
    #   - 2-1. i - 1 번째 와인을 마시는 경우
    #   - 2-2. i - 1 번째 와인을 마시지 않는 경우
    dp[i] = max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i])

print(dp[n])
