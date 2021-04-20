# 내 풀이
# 시간 복잡도: O(N)


def solution(absolutes, signs):
    answer = 0

    for num, sign in zip(absolutes, signs):
        answer += num if sign else -num

    return answer
