# 내 풀이
# 고민하는 점: 그래프 데이터를 인접한 노드 정보를 저장하는 식으로 받았는데, 더 효율적으로 입력을 받을 수 있는 방법이 없을지 고민된다.

from collections import deque
import sys

input = sys.stdin.readline  # 조금 더 빠르게 입력 받기

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# graph의 각각 노드에 대하여 인접한 노드 정보를 오름차순으로 정렬
for i in range(n + 1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)  # dfs 방문 정보를 담을 배열 생성
bfs_visited = [False] * (n + 1)  # bfs 방문 정보를 담을 배열 생성


# dfs 정의
def dfs(visited, graph, node):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            dfs(visited, graph, i)


# bfs 정의
def bfs(visited, graph, node):
    queue = deque([node])
    visited[node] = True
    while queue:
        e = queue.popleft()
        print(e, end=' ')
        for i in graph[e]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(dfs_visited, graph, v)
print()
bfs(bfs_visited, graph, v)
