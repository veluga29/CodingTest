# 내 풀이 - Pypy에서 성공
# 개선할 점: 문제는 잘 풀었지만, 플로이드 워셜을 수행할 때 인접행렬에서 자기자신으로 가는 부분을 0으로 초기화하지 않으면, 싸이클을 찾는 알고리즘을 더욱 효율적으로 짤 수 있음을 알았다.

import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for _ in range(v + 1)]  # 인접행렬 생성

# 간선 정보 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_cost = INF  # 최소 비용 싸이클 변수
# 자기자신으로 향하는 부분들만 비교하여 최소 비용 싸이클을 탐색
for i in range(1, v + 1):
    min_cost = min(min_cost, graph[i][i])

# 결과 출력
if min_cost == INF:
    print(-1)
else:
    print(min_cost)

# 초기 답안 - Pypy에서 성공
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# v, e = map(int, input().split())
# graph = [[INF] * (v + 1) for _ in range(v + 1)]  # 인접행렬 생성
#
# # 간선 정보 입력 받기
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#
# # 자기자신으로 향하는 부분을 0으로 초기화
# for i in range(1, v + 1):
#     graph[i][i] = 0
#
# # 플로이드 워셜 알고리즘 수행
# for k in range(1, v + 1):
#     for i in range(1, v + 1):
#         for j in range(1, v + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# min_cost = INF  # 최소 비용 싸이클 변수
# # 모든 싸이클 탐색
# for i in range(1, v + 1):
#     for j in range(1, v + 1):
#         if i == j:  # 자기자신으로 향하는 부분은 무시
#             continue
#         # 싸이클을 비교해 최소 비용 싸이클 갱신
#         min_cost = min(min_cost, graph[i][j] + graph[j][i])
#
# # 결과 출력
# if min_cost == INF:
#     print(-1)
# else:
#     print(min_cost)
