# 내 풀이
import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
# 인접 행렬을 생성하고 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 각 간선 정보를 입력 받고 테이블을 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 도시를 향하는 동일한 간선이 존재하는 경우, 비용이 적은 간선을 선택
    if graph[a][b] < c:
        continue
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행된 결과를 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 도달할 수 없는 경우, 0으로 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        # 도달할 수 있는 경우, 거리 출력
        else:
            print(graph[i][j], end=' ')
    print()
