# 내 풀이
point = input()

# 현재 위치 정수로 표현
x = int(point[1])
y = ord(point[0]) - 96

# 나이트가 가능한 8가지 이동 방향
dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, -1, 1, -1, 1]

result = 0

# 나이트가 8가지 방향 중 이동 가능한 경우의 수 확인
for i in range(8):
    mx = x + dx[i]
    my = y + dy[i]
    if mx >= 1 and mx <= 8 and my >= 1 and my <= 8:
        result += 1

print(result)

# 또 다른 접근
## 나이트가 가능한 8가지 이동 방향 (튜플로)
# steps = [
#           (-2, -1), (-1, -2), (1, -2), (2, -1),
#           (2, 1), (1, 2), (-1, 2), (-2, 1)
#         ]
# for step in steps:
#     ...