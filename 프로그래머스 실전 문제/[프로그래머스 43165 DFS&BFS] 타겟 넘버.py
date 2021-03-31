# 내 풀이
# 생각해볼 점: 문제 풀이까지는 잘 도달했다. 다만, 조금만 연산이 장황해지면
# 시간초과 뜨는 테스트케이스가 있어 리팩토링에 시간이 많이 걸렸다.
# 시간 복잡도: 2ⁿ - n의 범위가 20까지라 가능했다.

from collections import deque


def solution(numbers, target):
    answer = 0
    # 큐 생성 및 초기화
    queue = deque([numbers[0], -numbers[0]])
    idx = 1

    # BFS 수행
    # numbers의 마지막 숫자를 더하고 뺄 때까지
    while idx < len(numbers):
        for _ in range(len(queue)):
            num = queue.popleft()
            # 해당 순서의 숫자를 더한 값과 뺀 값을 큐에 삽입
            queue.append(num + numbers[idx])
            queue.append(num - numbers[idx])
        idx += 1

    # 큐가 빌 때까지
    while queue:
        if queue.popleft() == target:
            answer += 1

    return answer
