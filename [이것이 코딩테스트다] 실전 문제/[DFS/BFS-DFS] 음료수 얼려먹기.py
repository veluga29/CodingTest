# 문제 풀이 실패

# 모범 답안
n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]


# DFS로 특정 노드를 방문하고 연결된 인접 노드들 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우를 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j):
            result += 1

print(result)
