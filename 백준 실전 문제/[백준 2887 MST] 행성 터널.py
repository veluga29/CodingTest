# 생각해볼 점: 처음에 combination으로 경우의 수를 구해 풀었는데, n이 100000개 정도라 메모리를 초과해버렸다.
# 이를 극복하기 위해서는 간선 정보를 고려하는 경우의 수를 줄이는 아이디어가 필요했는데,
# 비용을 고려하는 식의 특성을 이용해 x축, y축, z축 각각 (n - 1)개씩의 간선만 사용해서 크루스칼 알고리즘을 진행하니,
# 풀이하는데 문제가 없었다.

# 내 풀이 - 수정 답안
import sys

input = sys.stdin.readline


# 특정 원소가 속한 집합을 찾기 (Find 연산)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기 (Union 연산)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n= int(input())
loc = []  # 좌표를 입력 받을 리스트
edges = []  # 간선들을 저장할 리스트
parent = [i for i in range(n)]  # 부모 테이블 생성 및 초기화
result = 0  # 최종 비용

# 좌표 입력을 수행
for i in range(n):
    x, y, z = map(int, input().split())
    loc.append((x, y, z, i))

# x, y, z 각각에 대하여 정렬해서 총 3 * (n - 1)개의 간선을 고려
loc.sort(key=lambda x: x[0])
for i in range(n - 1):
    edges.append((loc[i + 1][0] - loc[i][0], loc[i][3], loc[i + 1][3]))
loc.sort(key=lambda x: x[1])
for i in range(n - 1):
    edges.append((loc[i + 1][1] - loc[i][1], loc[i][3], loc[i + 1][3]))
loc.sort(key=lambda x: x[2])
for i in range(n - 1):
    edges.append((loc[i + 1][2] - loc[i][2], loc[i][3], loc[i + 1][3]))

edges.sort()  # 비용순으로 오름차순 정렬

# 모든 간선을 확인하여
for edge in edges:
    cost, a, b = edge
    # 사이클이 생기지 않으면 최소 신장 트리로 편입
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 결과 출력
print(result)


# 내 풀이 2- 답은 맞지만 메모리 초과
# from itertools import combinations
# import sys
#
# input = sys.stdin.readline
#
#
# # 특정 원소가 속한 집합을 찾기 (Find 연산)
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# # 두 원소가 속한 집합을 합치기 (Union 연산)
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# n= int(input())
# loc = []  # 좌표를 입력 받을 리스트
# edges = []  # 간선들을 저장할 리스트
# parent = [i for i in range(n)]  # 부모 테이블 생성 및 초기화
# result = 0  # 최종 비용
#
# # 좌표 입력을 수행
# for i in range(n):
#     x, y, z = map(int, input().split())
#     loc.append((x, y, z, i))
#
# pairs = list(combinations(loc, 2))  # 각 점들을 2개씩 짝지어 리스트화
# # 각 점들의 쌍마다 비용을 구해 간선 정보로 변환
# for pair in pairs:
#     a, b = pair
#     cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
#     edges.append((cost, a[3], b[3]))
#
# edges.sort()  # 비용순으로 오름차순 정렬
#
# # 모든 간선을 확인하여
# for edge in edges:
#     cost, a, b = edge
#     # 사이클이 생기지 않으면 최소 신장 트리로 편입
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# # 결과 출력
# print(result)