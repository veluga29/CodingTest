# 내 풀이 - test case 통과 but 시간 초과
# 문제점 : 구현은 했어도 3중 for문을 사용해 시간이 초과됐다. 코드 논리도 명확하게 눈에 들어오진 않는다.
# 고려해 볼 점 : 완전 탐색 문제가 아니라면 최대한 3중 for문을 피하자.

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 처리를 기록할 리스트를 생성
visited = [False] * (n + 1)


# BFS 메서드를 정의
def bfs(k):
    # 출발 도시를 queue에 삽입하고 방문 처리
    queue = deque([x])
    visited[x] = True
    v_list = []
    # k번 만큼 탐색
    for _ in range(k):
        # queue가 빌 때까지 queue에 있는 노드를 꺼내서 v_list에 담음
        while queue:
            v = queue.popleft()
            v_list.append(v)
        # v_list의 노드들에서 갈 수 있는 인접 노드 탐색
        for i in v_list:
            for j in graph[i]:
                # 인접노드가 방문하지 않은 노드라면 queue 삽입하고 방문 처리
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True
        # v_list 리스트를 비움
        v_list.clear()

    # 만일 queue에 최단 거리가 K인 도시가 담겨 있지 않다면 queue에 -1을 삽입함
    if not queue:
        queue.append(-1)

    # 최단 거리가 K인 도시들이 담긴 queue를 리스트화하고 오름차순으로 정리
    result = sorted(list(queue))

    return result


result = bfs(k)

for i in result:
    print(i)


# 지향할 답안
# from collections import deque
#
# n, m, k, x = map(int, input().split())
#
# graph = [[] for _ in range(n + 1)]
#
# # 모든 도로 정보 입력 받기
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# # 모든 도시에 대한 최단 거리 초기화
# distance = [-1] * (n + 1)
# distance[x] = 0  # 출발 도시의 최단 거리는 0으로 설정
#
# # BFS 수행
# q = deque([x])
# while q:
#     now = q.popleft()
#     # 현재 도시에서 이동 가능한 도시 확인
#     for next_node in graph[now]:
#         # 아직 방문하지 않은 도시라면
#         if distance[next_node] == -1:
#             # 최단 거리 갱신
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)
#
# # 최단 거리가 K인 모든 도시를 오름차순으로 출력
# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True
#
# # 최단 거리가 K인 도시가 없다면, -1을 출력
# if not check:
#     print(-1)
