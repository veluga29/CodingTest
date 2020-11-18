# 내 풀이


# 이진 탐색 함수 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 yes를 출력
        if array[mid] == target:
            return "yes"
        # 중간점의 값이 찾는 값보다 큰 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값이 찾는 값보다 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return "no"


n = int(input())
n_parts = list(map(int, input().split()))
m = int(input())
m_parts = list(map(int, input().split()))

n_parts.sort()  # 이진 탐색 수행을 위해 정렬함

# 손님이 확인을 요청한 부품마다 이진 탐색 수행
for part in m_parts:
    print(binary_search(n_parts, part, 0, n - 1), end=' ')
