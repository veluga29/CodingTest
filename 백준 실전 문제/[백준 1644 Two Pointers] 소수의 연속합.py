# 내 풀이
# 접근 방법: N의 최대 입력을 고려하여, 에라토스테네스 체를 사용해 소수들만 분류한다. 그리고 투 포인터 알고리즘을 사용해, 연속된 소수의 합이 n인 경우의 수를 모두 센다.
# 생각해볼 점: 시간 복잡도가 O(NloglogN)이라 결과적으론 잘 통과하지만, 연산 수가 많아 조금 느리다. Pypy에서는 1초이내로 마무리된다.
# 시간 복잡도: O(NloglogN) - 에라토스테네스의 체 알고리즘 수행이 제일 오래 걸리므로

# 2부터 4000000까지의 모든 수에 대하여 소수 판별 (n의 최대 입력)
limit_num = 4000000
# 처음엔 모든 수를 소수(True)인 것으로 초기화(0, 1은 제외)
array = [True for _ in range(limit_num + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 limit_num의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(limit_num ** 0.5) + 1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= limit_num:
            array[i * j] = False
            j += 1

# 판별된 소수를 새로운 리스트에 담음
prime_nums = []
for i in range(2, limit_num + 1):
    if array[i]:
        prime_nums.append(i)

# n 입력 받기
n = int(input())

p_len = len(prime_nums)  # 소수의 총 개수
result = 0  # 연속된 소수의 합이 n인 모든 경우의 수
interval_sum = 0  # 현재 부분합
end = 0

# start를 차례대로 증가시키며 반복
for start in range(p_len):
    # end를 가능한 만큼 이동시키기
    while interval_sum < n and end < p_len:
        interval_sum += prime_nums[end]
        end += 1
    # 부분합이 n일 때 카운트 증가
    if interval_sum == n:
        result += 1
    interval_sum -= prime_nums[start]

# 결과 출력
print(result)
