# 생각해볼 점: 힙생성 명령을 잊고 하나하나 담아버렸는데 heapify() 메서드를 기억하자.
# 또 중간에 안 넣어도 될 조건을 넣었는데, 시간에 촉박하면 코딩테스트 때도 그럴 수 있겠다는 생각이 드니 유의하자.
# 시간 복잡도: O(NlogN) - 힙 정렬 수행 시간

# 내 풀이
# import heapq
#
#
# def solution(scoville, K):
#     answer = 0
#     # 최소 힙 생성하기
#     h = []
#     for i in scoville:
#         heapq.heappush(h, i)
#
#     while True:
#         low1 = heapq.heappop(h)
#         # 첫 번째 원소가 K보다 크거나 같다면, 루프를 탈출하고 최소 횟수 리턴
#         if low1 >= K:
#             break
#         # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우, -1 리턴
#         if not h:
#             return -1
#
#         low2 = heapq.heappop(h)
#         # 가장 덜 매운 두 요소의 스코빌 지수가 0이라면, -1 리턴
#         if low1 == 0 and low2 == 0:
#             return -1
#
#         mixed_s = low1 + 2 * low2
#         heapq.heappush(h, mixed_s)
#         answer += 1
#
#     return answer


# 수정 답안
import heapq


def solution(scoville, K):
    answer = 0
    # 최소 힙 생성하기
    heapq.heapify(scoville)

    while True:
        low1 = heapq.heappop(scoville)
        # 첫 번째 원소가 K보다 크거나 같다면, 루프를 탈출하고 최소 횟수 리턴
        if low1 >= K:
            break
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우, -1 리턴
        if not scoville:
            return -1

        low2 = heapq.heappop(scoville)

        mixed_s = low1 + 2 * low2
        heapq.heappush(scoville, mixed_s)
        answer += 1

    return answer
