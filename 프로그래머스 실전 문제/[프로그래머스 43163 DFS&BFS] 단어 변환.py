from collections import deque


def check_words(word, cmp_word):
    cnt = 0
    for i in range(len(word)):
        if word[i] != cmp_word[i]:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        return True
    return False


def dfs(words, w, n):
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue


def solution(begin, target, words):
    answer = 0

    n = len(words)
    visited = [[False] * n for _ in range(n)]

    queue = deque([begin])

    while queue:
        w = queue.popleft()
        if w != begin:
            pass
        for i in range(n):
            if visited[i]

    return answer