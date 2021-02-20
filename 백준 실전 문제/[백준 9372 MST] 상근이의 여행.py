# 생각해볼 점: 최소 신장 트리 문제는 아니고 단순한 신장 트리를 구하는 문제였다.
# 그러다보니 문제에서 의도하는 방향은 내 풀이 1번일텐데, 내 풀이 2번처럼 신장 트리의 특성을 사용해 간단하게 풀 수도 있었다.
# 신장 트리의 간선 수는 모든 노드의 개수 - 1 이기 때문에 사실 무언가 알고리즘 설계 없이도 답은 구할 수 있다.

# 내 풀이 1
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    cnt = 0
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            cnt += 1
    print(cnt)

# 내 풀이 2
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     for _ in range(m):
#         a, b = map(int, input().split())
#     print(n - 1)
