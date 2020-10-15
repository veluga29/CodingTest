# 내 풀이
# 문제점 : 논리적이지만 모범 답안에 비해 너무 긴 점이 아쉽다. 그런데 진짜 문제는 지향할 답안이 이해가 안간다.

from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

values = set()  # 주어진 동전들로 만들 수 있는 금액들을 담을 집합

# 주어진 동전들 중 1개 ~ N개를 뽑아 만들 수 있는 모든 경우의 수를 구함
for i in range(1, n + 1):
    data = combinations(coins, i)
    # 구한 경우의 수의 해당하는 동전으로 만들 수 있는 금액을 values에 담음(집합이므로 중복 되지 않게 저장됨)
    for case in data:
        values.add(sum(case))

# 집합을 list화 하여 적은 금액 순으로 정렬함
values_list = list(values)
values_list.sort()

result = 1  # 1원부터 비교

# 주어진 동전들로 만들 수 있는 모든 금액에 포함되지 않는 최저 금액을 구함
while True:
    if result not in values_list:
        break
    result += 1

print(result)

# 지향할 답안
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# target = 1
# for x in data:
#     # 만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x
#
# # 만들 수 없는 금액 출력
# print(target)