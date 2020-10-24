# 내 풀이 - 문제 풀이 실패, 수정 답안
# 주목할 점 :
# 1. 자물쇠를 3배의 크기로 늘리고 남는 부분을 초기화해 사용 (내 접근은 key를 모든 경우에 대해 슬라이싱으로 처리하려 했는데 구현이 어려웠음)
# 2. 모범답안은 5중 for문으로 구현된 점 (문제 풀 때 for문은 절대 depth가 깊어지면 안된다는 경직된 사고로 더 나아가지 못함.)
# -> 답안은 시간 복잡도가 O(N²M²)이지만 N이 최대 20, M이 최대 20이므로 16만 정도 연산은 시간 초과없이 충분히 빠르게 수행할 수 있다.


# 시계 방향으로 90도 회전
def turn(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            result[j][m - 1 - i] = key[i][j]

    return result


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n):
        for j in range(n):
            if new_lock[n + i][n + j] != 1:
                return False
    return True


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠 중앙에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # 90도씩 4번 회전
    for turning in range(4):
        key = turn(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 자물쇠에 열쇠가 잘 들어갔는지 확인
                if check(new_lock):
                    answer = True
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return answer
