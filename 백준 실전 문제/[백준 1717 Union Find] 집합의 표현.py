# 내 풀이
# 생각해볼 점: 나의 경우 재귀 제한을 풀어야 문제가 풀렸는데, 다른 답안들은 이에 상관없이 문제를 푼 느낌이다. 고민해볼 점이다.

import sys
input = sys.stdin.readline
limit_number = 100000
sys.setrecursionlimit(limit_number)  # 재귀 제한을 여유 있게 해제


# 특정 원소가 속한 집합을 찾기 (Find 연산)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
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
parent = [i for i in range(n + 1)]  # 부모 테이블 생성 및 초기화

# 요구하는 연산 수행
for i in range(m):
    op, a, b = map(int, input().split())
    if op:  # 찾기 연산일 경우
        print('YES') if find_parent(parent, a) == find_parent(parent, b) else print('NO')
    else:  # 합치기 연산일 경우
        union_parent(parent, a, b)
