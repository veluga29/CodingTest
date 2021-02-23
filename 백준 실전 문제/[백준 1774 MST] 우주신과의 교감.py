from itertools import combinations
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


n, m = map(int, input().split())
loc = []  # 좌표를 입력 받을 리스트
edges = []  # 간선들을 저장할 리스트
parent = [i for i in range(n + 1)]  # 부모 테이블 생성 및 초기화
result = 0  # 최종 비용

# 좌표 입력을 수행
for i in range(n):
    x, y = map(int, input().split())
    loc.append((x, y, i + 1))

pairs = list(combinations(loc, 2))  # 각 점들을 2개씩 짝지어 리스트화
# 각 점들의 쌍마다 비용을 구해 간선 정보로 변환
for pair in pairs:
    a, b = pair
    cost = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    edges.append((cost, a[2], b[2]))

# 이미 연결된 통로를 확인하여 최소 신장 트리에 편입
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

edges.sort()  # 비용순으로 오름차순 정렬

# 모든 간선을 확인하여
for edge in edges:
    cost, a, b = edge
    # 사이클이 생기지 않으면 최소 신장 트리로 편입
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

# 결과 출력
print(f'{result:.2f}')
