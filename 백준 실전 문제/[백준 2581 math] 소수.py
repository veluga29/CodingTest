# 내 풀이
# 시간 복잡도: O(NloglogN) - 에라토스테네스의 체 알고리즘의 시간 복잡도

m = int(input())
n = int(input())

# 처음엔 모두가 소수인 것으로 초기화 (0과 1 제외)
array = [True for _ in range(n + 1)]
array[0], array[1] = False, False

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(n ** 0.5) + 1):
    if array[i]:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

p_sum = 0  # 범위 내 소수들의 합
p_min = int(1e4) + 1  # 범위 내 소수 중 최솟값

# 범위 내 소수들의 합과 최솟값을 구함
for i in range(m, n + 1):
    if array[i]:
        p_sum += i
        p_min = min(p_min, i)

# 범위 안에 소수가 없는 경우
if p_sum == 0:
    print(-1)
# 결과 출력
else:
    print(p_sum)
    print(p_min)
