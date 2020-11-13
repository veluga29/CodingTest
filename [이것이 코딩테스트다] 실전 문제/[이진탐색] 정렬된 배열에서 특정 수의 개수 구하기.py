# 내 풀이
from bisect import bisect_left, bisect_right


def count_x(array, x):
    left_idx = bisect_left(array, x)  # 정렬된 배열에 x를 삽입할 가장 왼쪽 인덱스 찾기
    right_idx = bisect_right(array, x)  # 정렬된 배열에 x를 삽입할 가장 왼쪽 인덱스 찾기
    return right_idx - left_idx  # x의 개수


n, x = map(int, input().split())
numbers = list(map(int, input().split()))

result = count_x(numbers, x)
# result 값이 0인 경우, -1 리턴
if not result:
    print(-1)
else:
    print(result)
