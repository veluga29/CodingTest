# 내 풀이
from bisect import bisect_right


def search_max_h(array, n, m):
    # 가장 뒤의 높이부터 계산 시작
    for h in range(heights[-1], 0, -1):
        result = 0
        # h보다 큰 높이가 시작되는 높이의 index를 구함
        min_idx = bisect_right(heights, h)
        for i in range(min_idx, n):
            result += heights[i] - h  # h보다 큰 떡들만 절단
        # 절단한 떡들의 길이가 손님의 요청한 길이보다 크거나 같다면
        if result >= m:
            return h  # h 최대값 리턴


n, m = map(int, input().split())
heights = sorted(list(map(int, input().split())))

print(search_max_h(heights, n, m))

# 모범답안
# n, m = map(int, input().split())
# array = list(map(int, input().split()))
#
# # 이진 탐색을 위한 시작점과 끝점 설정
# start = 0
# end = max(array)
#
# # 이진 탐색 수행
# result = 0
# while start <= end:
#     total = 0
#     mid = (start + end) // 2
#     for x in array:
#         # 잘랐을 때의 떡의 양 계산
#         if x > mid:
#             total += x - mid
#     # 떡의 양이 부족한 경우 더 많이 자르기
#     if total < m:
#         end = mid - 1
#     # 떡의 양이 충분한 경우 덜 자르기
#     else:
#         result = mid  # 최대한 덜 잘랐을 때가 답이므로, 여기서 길이 기록
#         start = mid + 1
#
# print(result)
