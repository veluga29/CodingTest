# 내 풀이
import sys
input = sys.stdin.readline


# 특정 원소가 속한 집합을 찾기 (Find 연산)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
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

turn = 0  # 첫 번째 사이클이 생긴 차례의 번호
cycle = False  # 사이클 생성 여부
parent = [i for i in range(n)]  # 부모 테이블 생성 및 초기화

for i in range(m):
    a, b = map(int, input().split())
    # 두 원소가 이어질 때 사이클이 생기고, 그것이 첫 번째 사이클일 경우
    if find_parent(parent, a) == find_parent(parent, b) and not cycle:
        turn = i + 1
        cycle = True
    union_parent(parent, a, b)  # 합치기 연산 수행

# 결과 출력
print(turn)
