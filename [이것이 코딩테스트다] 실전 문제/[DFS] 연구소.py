# 내 풀이 - Pypy에서 2초 내 수행, Python3에서 3.8초
# 문제점 : DFS를 간편히 수행하기위해 (*) 부분을 삽입했지만 논리적 흐름으로는 약간 부자연스럽다.
# 해결책 : 방향 벡터를 DFS에 적용해볼 것
# ex)
# def virus(x, y):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
#         if nx >= 0 and nx < n and ny >= 0 and ny < m:
#             if temp[nx][ny] == 0:
#                 # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
#                 temp[nx][ny] = 2
#                 virus(nx, ny)

from itertools import combinations
import copy

n, m = map(int, input().split())

board = []  # 연구소의 공간 정보를 담는 리스트
viruses = []  # 바이러스 위치 정보를 담는 리스트
spaces = []  # 빈 공간의 위치를 담는 리스트

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        # 빈공간의 위치를 저장
        if board[i][j] == 0:
            spaces.append((i, j))
        # 바이러스의 위치를 저장
        if board[i][j] == 2:
            viruses.append((i, j))


# DFS 함수 정의
def dfs(x, y, tmp_board):
    # 공간을 벗어나면 종료
    if x < 0 or y < 0 or x >= n or y >= m:
        return

    # 빈 공간이라면 증식
    if tmp_board[x][y] == 0:
        tmp_board[x][y] = 2

        # 동서남북 방향으로 dfs를 재귀적으로 호출
        dfs(x + 1, y, tmp_board)
        dfs(x, y - 1, tmp_board)
        dfs(x - 1, y, tmp_board)
        dfs(x, y + 1, tmp_board)

        return

    return


max_region = 0  # 안전 영역의 최대 크기 정의

# 빈 공간에서 3개의 벽을 세울 수 있는 모든 경우의 수
for data in combinations(spaces, 3):
    # 연구소 공간 정보를 복사하여 활용
    tmp_board = copy.deepcopy(board)

    # 복사한 공간 정보에 3개의 벽을 세움
    for x, y in data:
        tmp_board[x][y] = 1
    # 각각의 바이러스 위치에서 DFS 수행
    for x, y in viruses:
        # dfs 수행을 위해 바이러스 위치의 초기값을 잠시 0으로 바꿔 줌 (*)
        tmp_board[x][y] = 0
        # DFS 수행하여 바이러스 증식
        dfs(x, y, tmp_board)

    # 벽을 세우는 경우의 수마다 안전 영역 계산
    count = 0

    for i in range(n):
        for j in range(m):
            if tmp_board[i][j] == 0:
                count += 1

    # 안전 영역의 최대 크기 갱신
    max_region = max(count, max_region)

print(max_region)
