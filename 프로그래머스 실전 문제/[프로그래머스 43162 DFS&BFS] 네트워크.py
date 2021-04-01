# 내 풀이
# 접근법: 방문 정보 테이블을 하나씩 확인하면서, 아직 방문하지 않은 노드가 있다면
# DFS를 수행하고 네트워크 개수를 하나 센다.
# 시간 복잡도: O(N²) - 네트워크마다 DFS가 수행되지만
# 결국 다 합치면 인접 행렬 방식의 DFS 시간 복잡도가 된다.


# DFS 정의
def dfs(computers, v, visited, n):
    # 현재 노드를 방문
    visited[v] = True
    # 현재 노드의 인접 노드를 재귀적으로 방문
    for i in range(n):
        if computers[v][i] and not visited[i]:
            dfs(computers, i, visited, n)


def solution(n, computers):
    answer = 0
    visited = [False] * n  # 각 노드의 방문 정보를 표현

    # 첫번째 노드부터 순서대로 확인
    for v in range(n):
        # 아직 방문하지 않은 노드라면
        if not visited[v]:
            # dfs를 수행하고 네트워크 수를 하나 셈
            dfs(computers, v, visited, n)
            answer += 1

    return answer
