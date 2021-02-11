# 내 풀이
n, m = map(int, input().split())
nums = list(map(int, input().split()))  # 카드 숫자 입력 받기

result = 0  # M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합
# 전체 카드 숫자 중 3개를 뽑는 모든 경우의 수를 완전 탐색해 비교
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            pick_sum = nums[i] + nums[j] + nums[k]
            if result < pick_sum and pick_sum <= m:
                result = pick_sum

# 결과 출력
print(result)
