# 내 풀이
def solution(participant, completion):
    answer = ''
    # 두 배열을 오름차순으로 정렬
    participant.sort()
    completion.sort()

    # 완주한 선수들의 숫자만큼 비교
    for i in range(len(completion)):
        # 두 배열의 동일한 인덱스에 해당하는 값이 서로 다르다면
        if participant[i] != completion[i]:
            answer = participant[i]  # 해당 인덱스의 participant 값이 완주하지 못한 선수 이름
            return answer

    # answer가 빈 문자열이라면
    if not answer:
        # participant 배열의 마지막 값이 완주하지 못한 선수 이름
        answer = participant[len(participant) - 1]

    return answer
