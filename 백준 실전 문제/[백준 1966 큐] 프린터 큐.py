# 내 풀이
from collections import deque

t = int(input())
for num in range(t):
    n, m = map(int, input().split())
    # 문서마다 중요도 입력 받음
    importance = list(map(int, input().split()))
    # 각 문서의 순서와 중요도를 묶은 튜플을 원소로 갖는 큐 생성
    queue = deque(enumerate(importance))
    cnt = 0  # 인쇄 횟수 저장
    while queue:
        pass_print = False
        idx, val = queue.popleft()
        # 만일 큐의 가장 앞 문서의 중요도보다 중요도가 높은 문서가 존재한다면
        for i in range(len(queue)):
            if queue[i][1] > val:
                queue.append((idx, val))  # 가장 앞 문서를 큐의 가장 뒤로 보냄
                pass_print = True
                break
        if pass_print:
            continue
        cnt += 1
        # 원하는 문서를 찾으면 몇 번째에 인쇄되었는지 출력
        if idx == m:
            print(cnt)
            break
