# 내 풀이
# 고려해볼 점: 방향벡터의 또 다른 방법으로 ```for next_step in (v-1, v+1, v*2):```을 생각해볼 수 있다.
from collections import deque

n, k = map(int, input().split())
table = [0] * 100001  # 위치를 이동할 수직선 생성


# BFS 함수 정의
def bfs(x):
    queue = deque([x])  # 큐 생성
    # 걷기와 순간이동을 수행할 방향 벡터 생성
    dx = [1, 1, 2]
    op = ['-', '+', '*']

    while queue:
        p = queue.popleft()
        # 걷거나 순간이동하는 경우의 수 고려
        for i in range(3):
            np = eval(str(p) + op[i] + str(dx[i]))
            # 범위를 벗어나면 무시
            if np < 0 or np > 100000 or np == x:
                continue
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 최단거리 기록
            if table[np] == 0:
                queue.append(np)
                table[np] = table[p] + 1


bfs(n)  # BFS 수행
print(table[k])  # k까지의 최단거리 출력
