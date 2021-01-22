# 내 풀이 - 문제 풀이 실패, 수정답안
# 생각해본 점:
# 1. 다른 문제에 비해 다이나믹 프로그래밍이 더 어렵다고 느껴졌다. 이전에 관련 문제를 몇 번 풀어봤음에도 해법이 잘 생각나지 않아 연습을 많이 해야 할 것 같다.
# 2. 모범 답안에서 dp 테이블을 따로 만들지 않고 효율적으로 처리한 점 주목하자.

n = int(input())

rgb = [[]]  # 비용이 인덱스 1번부터 시작되도록 인덱스 0에 빈 리스트 추가
for _ in range(n):
    rgb.append(list(map(int, input().split())))

# 각각의 색에 대하여 dp 테이블 생성 및 초기화
dp_r = [0] * 1001
dp_g = [0] * 1001
dp_b = [0] * 1001
dp_r[1] = rgb[1][0]
dp_g[1] = rgb[1][1]
dp_b[1] = rgb[1][2]

# 바텀업 다이나믹 프로그래밍 수행
for i in range(2, n + 1):
    dp_r[i] = min(dp_g[i - 1], dp_b[i - 1]) + rgb[i][0]
    dp_g[i] = min(dp_r[i - 1], dp_b[i - 1]) + rgb[i][1]
    dp_b[i] = min(dp_r[i - 1], dp_g[i - 1]) + rgb[i][2]

# 빨강, 초록, 파랑 각각으로 n번째 집을 칠한 경우 중, 최소 비용을 찾아 출력
print(min(dp_r[n], dp_g[n], dp_b[n]))

# 모범 답안
# n = int(input())
# p = []
# for i in range(n):
#     p.append(list(map(int, input().split())))
# # 따로 dp 테이블 만들지 않고 입력받은 리스트에 바로 처리한 점 주목하자!
# for i in range(1, len(p)):
#     p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
# print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
