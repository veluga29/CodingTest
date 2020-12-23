# 내 풀이
def solution(answers):
    answer = []
    pattern_1 = [1, 2, 3, 4, 5]  # 1번 수포자가 찍는 방식
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 2번 수포자가 찍는 방식
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자가 찍는 방식
    scores = [0] * 3  # 1번, 2번, 3번 수포자의 점수를 담는 리스트

    # 수포자 1의 점수를 scores 배열의 인덱스 0에, 2의 점수를 인덱스 1에, 3의 점수를 인덱스 2에 계산하여 담음
    for i in range(len(answers)):
        if pattern_1[i % len(pattern_1)] == answers[i]:
            scores[0] += 1
        if pattern_2[i % len(pattern_2)] == answers[i]:
            scores[1] += 1
        if pattern_3[i % len(pattern_3)] == answers[i]:
            scores[2] += 1

    for i in range(len(scores)):
        # 모든 수포자 중 가장 높은 점수를 가진 수포자를 수포자 번호 기준 오름차순으로 answer 배열에 담음
        if scores[i] == max(scores):
            answer.append(i + 1)

    return answer
