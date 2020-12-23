# 내 풀이
def solution(array, commands):
    answer = []

    for command in commands:
        array_cut = array[command[0] - 1:command[1]]  # i번째부터 j번째까지 자르기
        array_cut.sort()  # 배열 정렬
        answer.append(array_cut[command[2] - 1])  # k번째 수를 answer에 담음

    return answer
