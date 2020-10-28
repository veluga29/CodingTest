# 내 풀이
# 개선할 방향 : 스테이지에 도달한 플레이어 수를 구할 때, for문을 쓰지 않고 가벼운 연산으로 구현하면 시간 복잡도가 더 줄었을 것이다.
# ex) length -= count

def solution(N, stages):
    answer = list(range(1, N + 1))  # 모든 스테이지를 원소로 가지는 리스트
    failures = [0] * (N + 1)  # 각 stage의 실패율을 담을 리스트 생성

    # 각각의 stage에 대하여 실패율을 계산
    for stage in range(1, N + 1):
        numerator = stages.count(stage)  # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수
        denominator = len([i for i in stages if i >= stage])  # 스테이지에 도달한 플레이어 수
        if denominator == 0:  # 스테이지에 도달한 유저가 없을 경우, 실패율은 0
            failure = 0
        else:
            failure = numerator / denominator
        failures[stage] = failure  # failures 리스트에 실패율 추가

    # 실패율이 높은 스테이지부터 내림차순, 실패율이 같은 경우 스테이지 번호에 대해 오름차순으로 정렬
    answer.sort(key=lambda x: (-failures[x], x))

    return answer
