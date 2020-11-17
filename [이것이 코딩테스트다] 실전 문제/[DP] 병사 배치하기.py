# 수정 답안 - 문제 풀이 실패
n = int(input())
array = list(map(int, input().split()))
array.reverse()  # '최장 증가 부분 수열' 문제로 변환

# DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외 병사 수 출력
print(n - max(dp))
