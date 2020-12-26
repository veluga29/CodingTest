# 내 풀이
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]


# dfs 정의
def dfs(x, y, cnt):
    if x < 0 or x >= n or y < 0 or y >= n:
        return cnt
    if graph[x][y] == 1:
        graph[x][y] = -1
        cnt += 1
        cnt = dfs(x - 1, y, cnt)
        cnt = dfs(x + 1, y, cnt)
        cnt = dfs(x, y - 1, cnt)
        cnt = dfs(x, y + 1, cnt)
        return cnt
    return cnt


h_cnt = 0  # 단지 개수
h_list = []  # 각 단지의 집의 개수
for i in range(n):
    for j in range(n):
        cnt = dfs(i, j, 0)
        if cnt:
            h_cnt += 1  # 단지 수 세기
            h_list.append(cnt)  # 단지 내 집의 개수 저장

print(h_cnt)
h_list.sort()  # 각 단지의 집 개수를 오름차순으로 정렬
for i in h_list:
    print(i)


# 또 다른 답안 - cnt를 전역변수로 사용
# n = int(input())
# graph = [list(map(int, input())) for _ in range(n)]
#
#
# # dfs 정의
# def dfs(x, y):
#     global cnt
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False
#     if graph[x][y] == 1:
#         graph[x][y] = -1
#         cnt += 1
#         dfs(x - 1, y)
#         dfs(x + 1, y)
#         dfs(x, y - 1)
#         dfs(x, y + 1)
#         return True
#     return False
#
#
# h_cnt = 0  # 단지 개수
# h_list = []  # 각 단지의 집의 개수
# for i in range(n):
#     for j in range(n):
#         cnt = 0
#         if dfs(i, j):
#             h_cnt += 1  # 단지 수 세기
#             h_list.append(cnt)  # 단지 내 집의 개수 저장
#
# print(h_cnt)
# h_list.sort()  # 각 단지의 집 개수를 오름차순으로 정렬
# for i in h_list:
#     print(i)
