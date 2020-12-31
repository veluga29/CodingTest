from collections import deque

n = int(input())
queue = deque([i for i in range(1, n + 1)])  # 카드 뭉치 생성

# 카드 뭉치의 카드가 1개가 될 때까지
while len(queue) > 1:
    queue.popleft()  # 맨 위의 카드를 버림
    queue.append(queue.popleft())  # 맨 위의 카드를 밑으로 옮김

print(queue[0])