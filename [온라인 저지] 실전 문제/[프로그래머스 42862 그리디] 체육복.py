# 내 풀이
def solution(n, lost, reserve):
    answer = 0
    status = [1] * n  # 각 학생이 가진 체육복 숫자의 상태표를 각각 1 값으로 초기화하여 리스트로 만듬

    for i in reserve:
        status[i - 1] = 2  # 여벌이 있는 학생은 체육복 수를 2로 갱신
    for i in lost:
        status[i - 1] -= 1  # 도난당한 학생은 체육복 수를 1개 차감

    # 상태표를 확인
    for idx, num in enumerate(status):
        # 체육복을 도난당한 학생의 앞 번호 학생에게 여벌의 체육복이 있다면 그 체육복을 먼저 빌려줌
        if idx - 1 >= 0 and num == 0 and status[idx - 1] == 2:
            status[idx - 1] -= 1
            status[idx] += 1
        # 체육복을 도난당한 학생의 뒷 번호 학생에게만 여벌의 체육복이 있다면 그 체육복을 빌려줌
        elif idx + 1 < n and num == 0 and status[idx + 1] == 2:
            status[idx + 1] -= 1
            status[idx] += 1

    # 상태표에서 체육복이 있는 학생의 수 세기
    for num in status:
        if num == 1 or num == 2:
            answer += 1

    return answer
