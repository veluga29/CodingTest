n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
x_list = list(map(int, input().split()))

# 수열 A를 정렬
a_list.sort()


# 이진 탐색 함수 정의
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return -1


for x in x_list:
    # 이진 탐색 수행
    result = binary_search(a_list, x, 0, n - 1)
    if result >= 0:
        print(1)
    else:
        print(0)
