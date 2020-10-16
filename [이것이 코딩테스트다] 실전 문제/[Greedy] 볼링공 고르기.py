# 내 풀이
# 주목해볼 점 : 조합의 수를 구할 때 for문으로 센 점을 기억하자. 지향할 답안 깔끔하니 참고하자.

from itertools import combinations

n, m = map(int, input().split())

balls = list(map(int, input().split()))

result = 0  # 경우의 수

# N개 중 2개 뽑는 모든 경우의 수 구하기
for i in combinations(balls, 2):
    result += 1

# 무게 1 ~ M 각각에 대하여 같은 무게의 공이 몇 개인지 세기
for weight in range(1, m + 1):
    same_num = balls.count(weight)
    # 같은 무게의 공이 없을 경우
    if same_num <= 1:
        continue
    # 같은 무게의 공이 있을 경우, 해당 무게의 공 중 2개를 뽑는 경우의 수를 구해서 전체 경우의 수에서 빼기
    for i in combinations(range(same_num), 2):
        result -= 1

print(result)

# 지향할 답안
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11
#
# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1
#
# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱해주기
#
# print(result)
