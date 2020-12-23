# 내 풀이
def solution(numbers):
    answer = set()  # 중복되는 값이 없게 탐색하기 위해서 빈 집합 생성

    # 숫자를 두 번 선택해 조합하는 방법을 모두 탐색
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:  # 서로 다른 인덱스라면 결과 값에 추가
                answer.add(numbers[i] + numbers[j])

    answer = list(answer)
    answer.sort()  # 오름차순으로 정렬

    return answer
