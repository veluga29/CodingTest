# 내 풀이
# 주목할 점: 리스트를 str()하면 괄호 그대로 '[x, x, ...]'로 변환됨을 기억하자!
n, k = map(int, input().split())
nums = [i for i in range(1, n + 1)]  # 1 ~ n까지의 수를 오름차순으로 생성
queue = []  # 요세푸스 순열을 저장할 리스트 생성
idx = 0

# nums가 빌 때까지
while nums:
    idx = (idx + k - 1) % len(nums)  # 수열에서 k번째 수의 인덱스 구하기
    queue.append(nums.pop(idx))  # k번째 수를 제거하고 순열로 만듬

print('<' + str(queue)[1:-1] + '>')
