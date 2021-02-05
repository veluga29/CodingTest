# 내 풀이
# 생각해 볼 점: 방향이 잡히지 않아 아이디어만 살짝 보고 풀었는데 답을 맞추고도 내가 푼 코드를 이해하는데 한참 걸렸다.
# LIS의 코드를 작성할 수 있지만 이해도가 떨어진 점이 문제였는데, 이 문제 덕에 보완해서 다행이었다.

n = int(input())

nums = list(map(int, input().split()))  # 수열 입력 받기

# 가장 긴 증가하는 부분 수열과 감소하는 부분 수열 각각을 위한 DP 테이블 생성 및 초기화
dp_asc = [1] * 1000
dp_desc = [1] * 1000

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if nums[i] > nums[j]:
            dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)

# 가장 긴 감소하는 부분 수열 알고리즘 수행
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if nums[i] > nums[j]:
            dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)

# 가장 긴 바이토닉 부분 수열의 길이 찾기
max_len = 0
for i in range(n):
    max_len = max(max_len, dp_asc[i] + dp_desc[i] - 1)  # 겹치는 부분 고려해서 1을 뺌

print(max_len)
