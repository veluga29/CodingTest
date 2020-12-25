# 내 풀이 - 테스트 케이스 한 개 통과 못함
def solution(name):
    answer = 0
    # print(ord('A'))  # 65
    # print(ord('Z'))  # 90

    table = [min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
             for i in range(len(name))]

    if sum(table) == 0:
        return answer

    cursor = 0
    left, right = 1, 1

    while True:
        answer += table[cursor]
        table[cursor] = 0

        if sum(table) == 0:
            return answer

        for i in range(1, len(table)):
            if table[cursor + i] == 0:
                right += 1
            else:
                break
        for i in range(1, len(table)):
            if table[cursor - i] == 0:
                left += 1
            else:
                break

        if left < right:
            cursor -= left
            answer += left
        else:
            cursor += right
            answer += right
