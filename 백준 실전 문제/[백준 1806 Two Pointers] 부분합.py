# 내 풀이
# 시간 복잡도: O(N)

n, s = map(int, input().split())
data = list(map(int, input().split()))

min_len = int(1e5)  # 구하고자 하는 부분 수열 중 가장 짧은 것의 길이
interval_sum = 0  # 현재 부분 수열의 부분합
end = 0

# 투 포인터 알고리즘 수행
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 s 이상인 부분 수열의 길이가 min_len보다 작다면
    if interval_sum >= s and end - start < min_len:
        min_len = end - start
    interval_sum -= data[start]

# min_len의 갱신이 없었다면 0 출력
if min_len == int(1e5):
    print(0)
# 최소 길이 출력
else:
    print(min_len)
