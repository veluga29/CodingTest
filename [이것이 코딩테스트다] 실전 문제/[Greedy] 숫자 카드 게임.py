# 내 풀이
# n, m = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# maxN = 0
#
# for row in data:
#     if maxN < min(row):
#         maxN = min(row)
#
# print(maxN)

# 개선한 답안
n, m = map(int, input().split())
maxN = 0

for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    maxN = max(maxN, min_value)

print(maxN)
