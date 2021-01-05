from collections import deque


# 큐를 왼쪽으로 회전시키는 함수 정의
def move_left(nums):
    nums.append(nums.popleft())


# 큐를 오른쪽으로 회전시키는 함수 정의
def move_right(nums):
    nums.appendleft(nums.pop())


n, m = map(int, input().split())
targets = list(map(int, input().split()))  # 뽑아내려는 원소의 위치
nums = deque([i + 1 for i in range(n)])  # 초기의 큐
result = 0  # 순환 횟수 저장

for target in targets:
    idx = nums.index(target)
    # 찾아야 하는 원소가 큐의 맨 앞에 있는 경우
    if idx == 0:
        nums.popleft()
        continue

    # 왼쪽으로 회전시키는 것이 이득인 경우
    if idx <= len(nums) // 2:
        for i in range(idx):
            move_left(nums)
        result += idx
    # 오른쪽으로 회전시키는 것이 이득인 경우
    else:
        for i in range(len(nums) - idx):
            move_right(nums)
        result += len(nums) - idx

    nums.popleft()

print(result)
