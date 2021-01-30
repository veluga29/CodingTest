# 내 풀이
n = int(input())
nums = list(map(int, input().split()))  # 수열 입력 받기

# DP 테이블 생성 및 초기화
dp = [1] * 1000

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 결과 출력
print(max(dp))
