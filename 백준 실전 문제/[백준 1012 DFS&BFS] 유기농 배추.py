# 내 풀이
# 주목할 점: dfs와 bfs 모두 풀 수 있었고, dfs의 경우 파이썬 3의 재귀 한도에 대해 알 수 있었다.

from collections import deque  # bfs를 위한 큐 생성 라이브러리
import sys
sys.setrecursionlimit(10000)  # 파이썬 재귀 한도를 10000으로 늘림 (기존 재귀 한도: 1000)


# dfs 정의
def dfs(x, y):
    graph[x][y] = -1
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
            continue
        if graph[next_x][next_y] == 1:
            dfs(next_x, next_y)


# bfs 정의
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = -1
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = -1


result = []  # 테스트 케이스마다 결과 저장
t = int(input())
# 테스트 케이스 수만큼 수행
for num in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]  # 배추밭 초기화

    # 배추의 위치 갱신
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0  # 배추흰지렁이의 개수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)  # dfs 혹은 bfs로 수행함
                cnt += 1  # 인접한 배추 한 무더기 당 하나의 배추흰지렁이 개수 세기
    result.append(cnt)

for i in result:
    print(i)
