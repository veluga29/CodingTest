# 내 풀이
from collections import deque

m, n, h = map(int, input().split())
# 토마토 상자를 3차원 리스트로 입력받음
box = []
for _ in range(h):
    box.append([list(map(int, input().split())) for _ in range(n)])
ripe = deque()  # 익은 토마토를 넣을 큐 생성


# BFS 함수 정의
def bfs():
    days = -1
    # 위, 아래, 상, 하, 좌, 우 방향 벡터 정의
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    # 토마토 익히기 수행
    while ripe:
        days += 1
        for _ in range(len(ripe)):
            x, y, z = ripe.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                # 범위를 넘어갈 경우 무시
                if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m:
                    continue
                # 인접한 곳에 안익은 토마토가 있을 경우, 익히고 큐에 담음
                if box[nx][ny][nz] == 0:
                    ripe.append((nx, ny, nz))
                    box[nx][ny][nz] = 1

    # 토마토를 다 익힌 후에도 익지 않은 토마토가 남아 있을 경우
    for b in box:
        for row in b:
            if 0 in row:
                return -1
    return days


# 초기에 존재하는 익은 토마토들을 큐에 담음
for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                ripe.append((k, i, j))

# BFS 수행 및 결과 출력
print(bfs())
