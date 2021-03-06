# 내 풀이 - 시간 초과, 수정 답안
# 생각해볼 점: 에라토스테네스의 체의 시간복잡도가 매우 빠르긴 하지만, 테스트케이스마다 매번 돌리는 것은 비효율적이었다.
# 한 번만 써도 되는데 괜히 시간 초과를 냈다.

n = 123456 * 2  # 2부터 (2 * 123456)까지의 모든 수에 대하여 소수 판별
# 처음엔 모든 수를 소수(True)인 것으로 초기화(0, 1은 제외)
array = [True for _ in range(2 * n + 1)]

# 에라토스테네스의 체 알고리즘 수행
# 2부터 2n의 제곱근까지의 모든 수에 대하여
for i in range(2, int((2 * n) ** 0.5) + 1):
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= 2 * n:
            array[i * j] = False
            j += 1

# 테스트 케이스 수행
while True:
    val = int(input())
    # 입력값이 0이면 종료
    if val == 0:
        break
    cnt = 0  # n보다 크고 2n보다 작거나 같은 소수의 개수
    # 범위에 해당하는 소수의 개수 세기
    for i in range(val + 1, 2 * val + 1):
        if i > 1 and array[i]:
            cnt += 1
    # 개수 출력
    print(cnt)
