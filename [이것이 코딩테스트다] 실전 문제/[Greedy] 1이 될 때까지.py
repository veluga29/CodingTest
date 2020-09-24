# 내 풀이
# n, k = map(int, input().split())
# result = 0
#
# while n > 1:
#   if n % k == 0:
#     n //= k
#     result += 1
#   else:
#     n -= 1
#     result += 1
#
# print(result)

# 지향할 답안
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나눠지는 수가 될 때까지 단번에 1씩 빼기 (기억하자!!)
    target = (n // k) * k
    result += (n - target)
    n = target
    # N을 K로 더 이상 나눌 수 없을 때 반복문 탈출
    if n < k:
        break
    # N을 K로 나눈다.
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1씩 빼기 (기억하자!!)
result += (n - 1)
print(result)