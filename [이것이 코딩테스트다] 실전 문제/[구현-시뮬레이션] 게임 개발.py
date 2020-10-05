# 내 풀이
# 문제점 : 전체적으로는 모범답안과 생각 흐름이 유사하지만, 내 풀이는 구현한 제어문의 depth가 깊다.
# 고려해 볼 점 : 내 풀이는 기존 input data 지도에 방문을 기록하며 구현한 반면, 모범 답안은 또 하나의 새로운 지도를 초기화해 방문한 지점을 표기했다. 기존 input data를 보존해 만드는 방법도 눈여겨 보자.

n, m = map(int, input().split())
x, y, d = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

# 앞에서부터 차례로 북동남서(0, 1, 2, 3) 방향 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 위치 방문 표시
world[x][y] = 1
result = 1
flag_d = d

while True:
    # 왼쪽 방향 돌아보기
    d -= 1
    if d < 0:
        d = 3

    next_x = x + dx[d]
    next_y = y + dy[d]

    # 갈 수 없는 곳일 때
    if world[next_x][next_y] == 1 or world[next_x][next_y] == 2:
        # 네 방향 모두 갈 수 없는 곳일 때
        if d == flag_d:
            back_x = x - dx[d]
            back_y = y - dx[d]
            # 뒷 방향이 바다일 때, 움직임을 멈춤
            if world[back_x][back_y] == 1:
                break
            # 뒷 방향이 육지일 때, 뒤로 한 칸 이동
            else:
                x -= dx[d]
                y -= dy[d]
                continue
        # 일반적으로 갈 수 없는 곳일 때 1단계로 돌아감
        else:
            continue
    # 갈 수 있는 곳이면 한 칸 이동해서 방문(2)
    else:
        x = next_x
        y = next_y
        world[next_x][next_y] = 2
        flag_d = d
        result += 1

print(result)
