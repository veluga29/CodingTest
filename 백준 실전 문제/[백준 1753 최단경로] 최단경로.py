# 내 풀이
import heapq
import sys

INF = 1e9  # 무한을 나타내는 값으로 10억 설정
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)]  # 인접 리스트 생성
distance = [INF] * (v + 1)  # 최단 거리 테이블을 생성하고 무한으로 초기화

# 간선 정보 입력 받기
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


# 다익스트라 알고리즘 정의
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리한 노드는 무시
        if distance[now] < dist:
            continue
        # 현재 노드에 인접한 노드 체크
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 경유해 가는 거리가 더 작다면 테이블 갱신
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(k)

# 수행 결과 출력
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)
