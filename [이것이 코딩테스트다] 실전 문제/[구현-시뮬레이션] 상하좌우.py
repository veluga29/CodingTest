# 내 풀이
# n = int(input())
# pList = input().split()
# x, y = 1, 1
#
# for i in pList:
#     if i == 'L' and y != 1:
#         y -= 1
#     if i == 'R' and y != n:
#         y += 1
#     if i == 'U' and x != 1:
#         x -= 1
#     if i == 'D' and x != n:
#         x += 1
# print(x, y)

# 지향할 풀이
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)