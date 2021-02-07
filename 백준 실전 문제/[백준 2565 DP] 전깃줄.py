# 내 풀이
# 접근 아이디어: 전깃줄 위치 정보를 A와 B 한 쪽을 기준으로 오름차순 정렬하고 반대 편 수열을 보면,
# 가장 긴 증가하는 부분 수열(LIS)을 찾는 것이 결과적으로 남겨야 할 전깃줄을 찾는 것이 된다.
n = int(input())

# 전깃줄의 위치 정보 입력 받음
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

# A의 위치를 기준으로 전깃줄 위치 정보를 오름차순 정렬
lines.sort(key=lambda x: x[0])

# DP 테이블 생성 및 초기화
dp = [1] * n

# B의 수열에서 가장 긴 증가하는 부분 수열(LIS) 찾기
for i in range(1, n):
    for j in range(0, i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# 없애야 하는 전깃줄의 최소 개수 구하기
print(n - max(dp))
