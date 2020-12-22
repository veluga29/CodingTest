# 내 풀이
# 문제점: 예외 케이스 하나를 삽입한 점이 코드 간결함을 떨어뜨려 아쉽다.
# 주목할 점: 모범 답안은 앞에서부터 탐색하여 cnt 없이 for문의 i만으로 h값을 찾아냄을 주목하자.


def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    cnt = 1
    # 뒤에서부터 h번 이상 인용된 논문이 h편 이상이 되는 위치 찾기
    for i in range(n - 1, -1, -1):
        if citations[i] < cnt:
            answer = cnt - 1
            break
        cnt += 1
    # h의 최댓값이 모든 논문의 개수일 경우
    if len(citations) == cnt - 1:
        answer = cnt - 1
    return answer

# 모범 답안
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0
