# 내 풀이
# 생각이 드는 점: 최단경로 문제들이 근간 알고리즘을 잘 외워두면 대체로 그것을 활용하는 측면에서 문제를 풀 수 있음을 느낀다.
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n + 1)  # 최단 거리 테이블 생성
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리한 노드인 경우 무시
        if distance[now] < dist:
            continue
        # 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 경유하는 것이 최단 거리인 경우, 인접한 노드 정보를 힙에 삽입하고 최단 거리 갱신
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost
    return distance  # 최단 거리 테이블 반환


T = int(input())
for _ in range(T):
    # 교차로, 도로, 목적지 후보 개수 입력 받기
    n, m, t = map(int, input().split())
    # 출발지 및 경유할 노드 두 개 입력 받기
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    # 간선 정보 입력 받기
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    x_list = []  # 목적지 후보들을 담을 리스트 생성
    for _ in range(t):
        x_list.append(int(input()))
    x_list.sort()  # 목적지 후보들을 오름차순으로 정렬

    # 출발지와 경유할 노드들에 대하여 각각 다익스트라 알고리즘 수행
    distance_s = dijkstra(s)
    distance_g = dijkstra(g)
    distance_h = dijkstra(h)

    # 목적지 후보마다 확인
    for x in x_list:
        org_cost = distance_s[x]  # 출발지에서 목적지까지의 최단 거리
        cmp_cost_1 = distance_s[g] + distance_g[h] + distance_h[x]  # 출발지 - g노드 - h노드 - 목적지 경로의 최단 거리
        cmp_cost_2 = distance_s[h] + distance_h[g] + distance_g[x]  # 출발지 - h노드 - g노드 - 목적지 경로의 최단 거리
        # 두 개의 경유 경로 중 하나라도 실제 최단 경로가 존재한다면, 해당 목적지를 출력
        if org_cost == cmp_cost_1 or org_cost == cmp_cost_2:
            print(x, end=' ')
    print()
