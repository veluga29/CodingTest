# 내 풀이
# 시간 복잡도: Nlog(N) - 정렬 수행 시간이 가장 오래 걸리므로

n = int(input())
data = list(map(int, input().split()))

min_val = 2 * int(10e9)  # 혼합 용액의 최소 특성값
left = 0
right = n - 1

data.sort()  # 오름차순 정렬

# 양 끝의 포인터가 엇갈리기 전까지
while left < right:
    # 현재 가리키는 두 용액의 특성값 합이 최소 특성값이라면 최솟값 갱신
    if abs(data[left] + data[right]) < min_val:
        min_val = abs(data[left] + data[right])
        min_pair = (data[left], data[right])
    # right가 가리키는 특성값의 절대값이 더 크다면 right를 1 감소시킴
    if abs(data[left]) < abs(data[right]):
        right -= 1
    # left가 가리키는 특성값의 절대값이 크거나 같다면 left를 1 증가시킴
    else:
        left += 1

# 특성값의 합이 최소인 두 용액의 특성값을 오름차순으로 출력
print(*min_pair)
