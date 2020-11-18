# 내 풀이
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 고정점을 찾은 경우
        if array[mid] == mid:
            return mid
        # 중간점의 값이 중간점보다 큰 경우 왼쪽 확인
        elif array[mid] > mid:
            end = mid - 1
        # 중간점의 값이 중간점보다 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return -1  # 고정점이 없는 경우 -1 반환


n = int(input())
numbers = list(map(int, input().split()))

print(binary_search(numbers, 0, n - 1))
