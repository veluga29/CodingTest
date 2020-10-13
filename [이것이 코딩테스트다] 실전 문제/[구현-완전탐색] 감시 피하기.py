# 내 풀이 - 문제 풀이 실패, 수정 답안
# 문제점 : 그래프 문제임을 확인하고 너무 BFS, DFS에 갇혀서 완전 탐색의 가능성을 시도해보지 못함

from itertools import combinations

n = int(input())

graph = []  # 공간 정보
teachers = []  # 선생님들의 좌표
spaces = []  # 빈 공간 좌표

# 공간 정보 입력
for i in range(n):
    graph.append(input().split())
    # 선생님 및 빈 공간 좌표 저장
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        if graph[i][j] == 'X':
            spaces.append((i, j))


# 특정 방향 감시 (학생 발견 : True, 학생 미발견 : False)
def watch(x, y, direction):
    # 동쪽 감시
    if direction == 0:
        while y < n:
            if graph[x][y] == 'S':  # 학생이 있는 경우
                return True
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return False
            y += 1
    # 북쪽 감시
    if direction == 1:
        while x > -1:
            if graph[x][y] == 'S':  # 학생이 있는 경우
                return True
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return False
            x -= 1
    # 서쪽 감시
    if direction == 2:
        while y > -1:
            if graph[x][y] == 'S':  # 학생이 있는 경우
                return True
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return False
            y -= 1
    # 남쪽 감시
    if direction == 3:
        while x < n:
            if graph[x][y] == 'S':  # 학생이 있는 경우
                return True
            if graph[x][y] == 'O':  # 장애물이 있는 경우
                return False
            x += 1
    return False


# 장애물 설치 이후, 학생 감시
def process():
    # 모든 선생님 위치에서
    for x, y in teachers:
        # 네 방향 감시
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


check = False  # 한 명도 감지되지 않게 장애물을 설치 가능한지 여부

# 빈 공간에 3개의 장애물을 설치할 수 있는 모든 경우의 수
for data in combinations(spaces, 3):
    # 장애물 설치
    for x, y in data:
        graph[x][y] = 'O'
    # 학생이 감지되지 않는 경우 확인 시, check를 기록하고 루프를 벗어남
    if not process():
        check = True
        break
    # 장애물 회수
    for x, y in data:
        graph[x][y] = 'X'

if check:
    print("YES")
else:
    print("NO")
