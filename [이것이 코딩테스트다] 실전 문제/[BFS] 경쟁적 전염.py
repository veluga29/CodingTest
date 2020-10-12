# 내 풀이 - 문제 풀이 실패, 수정 답안
# 의문점 : 바이러스의 정보를 튜플로 담을 때, 위치, 시간, 종류 순으로 정보를 담으면 백준에서 오류 발생... (종류, 시간, 위치 순은 문제 없음)

from collections import deque

n, k = map(int, input().split())

graph = []  # 시험관 정보를 담는 리스트
data = []  # 바이러스의 정보를 담는 리스트

# 시험관 정보 입력 받기
for i in range(n):
    # 시험관 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스의 종류, 시간, 위치를 저장
            data.append((graph[i][j], 0, i, j))

# 정렬 후 큐로 옮기기
data.sort()
queue = deque(data)

# S, X, Y 입력
target_s, target_x, target_y = map(int, input().split())

# 동북서남 방향 벡터 정의
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# BFS 수행
while queue:
    virus, s, x, y = queue.popleft()
    # queue가 비거나 S초가 지날 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 시험관을 벗어났을 때 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        # 아직 방문하지 않은 위치라면, 해당 위치에 바이러스 증식
        if graph[nx][ny] == 0:
            queue.append((virus, s + 1, nx, ny))
            graph[nx][ny] = virus

print(graph[target_x - 1][target_y - 1])
