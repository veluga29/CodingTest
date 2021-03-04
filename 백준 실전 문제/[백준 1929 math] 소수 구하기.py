# 내 풀이
# 생각해볼 점: 마지막 출력에서 1을 거르는 조건을 생각하지 못해 오래 걸렸다. 예외 케이스를 항상 염두하자.
m, n = map(int, input().split())

# 처음엔 모든 수를 소수(True)인 것으로 초기화(0, 1은 제외)
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(n ** 0.5) + 1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# m이상 n이하 소수 출력
for i in range(m, n + 1):
    if i > 1 and array[i]:
        print(i)
