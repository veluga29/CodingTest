# 내 풀이
from collections import deque


def solution(progresses, speeds):
    answer = []
    day = 0  # 일 수
    pro_queue = deque(progresses)
    sp_queue = deque(speeds)

    while pro_queue:
        day += 1  # 날짜 표시
        func_num = 0  # 하루에 배포한 기능 수
        # 하루 치 작업 진행
        for i in range(len(pro_queue)):
            if pro_queue[i] == 100:  # 작업 진도가 100이면 생략
                continue
            pro_queue[i] += sp_queue[i]  # 오늘치 작업 진도 진행
            if pro_queue[i] > 100:  # 작업 진도가 100을 넘었다면 100으로 설정
                pro_queue[i] = 100

        # 작업 진도 큐가 빌 때 까지
        while pro_queue:
            if pro_queue[0] >= 100:  # 가장 앞에 있는 기능의 작업 진도가 100이라면
                func_num += 1  # 기능 배포
                pro_queue.popleft()  # 큐에서 해당 기능을 내보냄
                sp_queue.popleft()
            else:
                break  # 가장 앞에 작업 진도 100인 기능이 없음

        # 오늘 배포한 기능 수를 배열에 담음
        if func_num:
            answer.append(func_num)

    return answer
