def dfs(graph, v, visited):
    # 현재 노드 방문
    visited[v] = True
    print(v, end=' ')
    # 현재 노드의 인접 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [6, 8],
    [1, 7]
]

# 각 노드의 방문 정보 표현
visited = [False] * 9

# DFS 함수 호출
dfs(graph, 1, visited)
