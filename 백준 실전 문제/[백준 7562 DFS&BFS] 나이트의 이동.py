from collections import deque


# BFS 함수 정의
def bfs(sx, sy, ex, ey):
    # 시작 지점이 목표 지점과 같은 경우, 함수 종료
    if sx == ex and sy == ey:
        return
    queue = deque([(sx, sy)])

    # 나이트가 움직일 수 있는 방향 벡터 정의
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        x, y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위를 벗어나는 경우, 무시
            if nx < 0 or nx >= i or ny < 0 or ny >= i:
                continue
            # 처음 도달하는 칸인 경우, 이동 횟수를 기록하고 해당 칸의 위치를 큐에 삽입
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


t = int(input())
# 테스트 케이스 수 만큼 반복
for _ in range(t):
    i = int(input())
    sx, sy = map(int, input().split())  # 나이트가 현재 있는 칸 입력 받기
    ex, ey = map(int, input().split())  # 나이트가 이동하려고 하는 칸 입력 받기

    graph = [[0] * i for _ in range(i)]  # i X i 크기의 체스판 생성

    # BFS 수행
    bfs(sx, sy, ex, ey)
    # 결과 출력
    print(graph[ex][ey])
