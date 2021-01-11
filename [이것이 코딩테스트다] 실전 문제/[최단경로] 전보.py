# 내 풀이
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정

n, m, c = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 생성하고 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드의 최단거리를 0으로 설정하고, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리한 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 가는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(c)

cnt = 0  # 도달할 수 있는 도시의 개수
result_time = 0  # 가장 시간이 오래걸리는 도시의 최단거리
for d in distance:
    # 도달할 수 있는 도시인 경우
    if d != INF:
        cnt += 1
        result_time = max(result_time, d)

# 시작 도시는 제외해야 하므로 cnt - 1 출력
print(cnt - 1, result_time)
