# 내 풀이
# n, m, k = map(int, input().split())
# arr = list(map(int, input().split()))
# arr.sort()
#
# # 가장 큰 수가 더해지는 횟수와 두 번째로 큰 수가 더해지는 횟수를 계산해 모두 합한다.
# a = arr[n-1] * (m // (k + 1)) * k
# b = arr[n-2] * (m // (k + 1))
# c = arr[n-1] * (m % (k + 1))
# result = a + b + c
#
# print(result)

# 지향할 답안
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

first = arr[n-1] # 가장 큰 수
second = arr[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)