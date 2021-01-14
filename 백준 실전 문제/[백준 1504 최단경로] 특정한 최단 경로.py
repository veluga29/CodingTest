# 내 풀이
# 고려해 볼 점: 한 노드에서 모든 노드로 가는 다익스트라를 3번 사용해 풀었는데, 한 노드에서 다른 한 노드로 가는 최단거리를 3번 구하는 방법도 있는지 궁금하다.

import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance_1 = [INF] * (n + 1)  # 출발노드가 1인 최단 거리 테이블 생성
distance_v1 = [INF] * (n + 1)  # 출발노드가 v1인 최단 거리 테이블 생성
distance_v2  = [INF] * (n + 1)  # 출발노드가 v2인 최단 거리 테이블 생성

# 간선 정보 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


# 다익스트라 알고리즘 정의
def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


# 1, v1, v2 노드 각각에 대하여 다익스트라 알고리즘 수행
dijkstra(1, distance_1)
dijkstra(v1, distance_v1)
dijkstra(v2, distance_v2)

# 1-v1-v2-n 경로와 1-v2-v1-n 경로의 최단거리 구하기
v1_v2_path = distance_1[v1] + distance_v1[v2] + distance_v2[n]
v2_v1_path = distance_1[v2] + distance_v2[v1] + distance_v1[n]
# 두 경로 중 가장 작은 값을 최단거리로 결정
result = min(v1_v2_path, v2_v1_path)

# 도달할 수 없는 경우 -1 출력
if result >= INF:
    print(-1)
# 도달할 수 있는 경우 최단거리 출력
else:
    print(result)
