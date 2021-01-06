# 내 풀이 - 문제 풀이 실패, 수정답안
# 문제점: bfs로 접근하는 것은 알았는데, 최소 날짜를 어떻게 구해야할지 도저히 감이 잡히지 않았다.
# 해결책: ```while ripe:```, ```for _ in range(len(ripe)):``` 이 두 코드가 막힌 부분을 해소해주었다.
from collections import deque


def bfs():
    # 동서남북 방향벡터 설정
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    days = -1  # while의 종료 조건으로 1씩 밀리기 때문에 0이 아닌 -1로 설정

    while ripe:
        days += 1
        # 현재 큐에 담긴 익은 토마토의 수만큼
        for _ in range(len(ripe)):
            x, y = ripe.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 익은 토마토 주변에 익지 않은 토마토가 있는 경우
                if box[nx][ny] == 0:
                    ripe.append((nx, ny))
                    box[nx][ny] = 1

    # 토마토가 모두 익지 못하는 경우
    for row in box:
        if 0 in row:
            return -1
    return days


m, n = map(int, input().split())  # n이 행, m이 열
box, ripe = [], deque()  # 상자 정보를 담는 리스트와 익은 토마토를 담는 큐를 생성
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(m):
        # 초기 익은 토마토를 큐에 담음
        if box[i][j] == 1:
            ripe.append((i, j))

# bfs를 수행하여 최소 날짜 출력
print(bfs())
