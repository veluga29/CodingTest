# 내 풀이
from collections import deque

n = int(input())
nums = deque([int(input()) for _ in range(n)])  # 주어진 수열을 큐 형태로 사용
stack = []
result = []

# 스택에 1 ~ n까지의 수를 오름차순으로 삽입
for i in range(1, n + 1):
    stack.append(i)
    result.append('+')
    # nums와 stack에 원소가 있고, nums의 첫번째 값이 stack의 최상단 값과 같다면
    while nums and stack and nums[0] == stack[-1]:
        stack.pop()  # 스택의 최상단 값 제거
        nums.popleft()  # 큐의 맨 앞에 있는 값 제거
        result.append('-')

# nums에 원소가 남아 있다면 'NO'를 출력
if nums:
    print("NO")
# nums가 비어있다면 result의 연산자들을 모두 출력
else:
    for i in result:
        print(i)
