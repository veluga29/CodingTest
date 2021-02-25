# 내 풀이
n = int(input())
nums = list(map(int, input().split()))

result = 0  # 소수의 개수

# 주어진 수들 각각에 대하여 연산 수행
for num in nums:
    # 1은 소수가 아니므로 제외
    if num == 1:
        continue
    check = True  # 소수 판별을 위한 flag
    # 1과 자기 자신을 제외한 모든 수에 대하여
    for i in range(2, num):
        # 나누어 떨어지면 소수가 아님
        if num % i == 0:
            check = False
            break
    # 소수라면 개수 count
    if check:
        result += 1

# 결과 출력
print(result)
