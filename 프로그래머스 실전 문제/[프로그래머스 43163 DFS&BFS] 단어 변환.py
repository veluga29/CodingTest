# 내 풀이
# 개선해볼 점: bfs 수행 전 큐를 초기화하는 코드가 좀 긴데, 이를 리팩토링할 수 있음 좋겠다.
# 또한, 방문 정보 테이블도 2차원 테이블로 해결했는데, 다른 방법도 생각해봐야겠다.
# 시간 복잡도: O(FNL) - F: begin에서 처음으로 변환하는 단어의 갯수, N: 단어의 집합 내 단어 갯수, L: 단어의 길이

from collections import deque


# 두 단어가 한 글자가 다른 관계인지 체크하는 함수 정의
def one_diff(word, cmp_word):
    cnt = 0
    for i in range(len(word)):
        if word[i] != cmp_word[i]:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    answer = 0

    n = len(words)
    visited = [[False] * n for _ in range(n)]  # 2차원 방문 정보 테이블

    # 큐 생성 및 초기화
    # begin과 철자가 하나만 다른 단어를 찾아, 방문 처리하고 큐에 삽입
    queue = deque()
    for i in range(n):
        if one_diff(begin, words[i]):
            visited[i][i] = True
            queue.append((i, i, 1))  # (단어의 인덱스, 방문 정보 리스트의 인덱스, 단계)

    # BFS 수행
    while queue:
        word_idx, visit_idx, level = queue.popleft()
        visited[visit_idx][word_idx] = True

        # 해당 단어가 target과 같으면, 해당 단어의 단계를 리턴
        if words[word_idx] == target:
            answer = level
            return answer

        for i in range(n):
            # 아직 방문하지 않은 단어이고 현재 단어랑 철자가 하나만 다르다면 큐에 삽입
            if not visited[visit_idx][i] and one_diff(words[word_idx], words[i]):
                queue.append((i, visit_idx, level + 1))

    return answer
