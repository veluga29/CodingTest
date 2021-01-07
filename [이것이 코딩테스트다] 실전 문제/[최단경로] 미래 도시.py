# 내 풀이
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정
n, m = map(int, input().split())
# 2차원 리스트로 인접행렬을 만들고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 그래프 정보를 입력받아 초기화
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 도달할 수 없는 경우, -1 출력
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(graph[1][k] + graph[k][x])
