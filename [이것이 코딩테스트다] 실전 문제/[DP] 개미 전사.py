# 내 풀이
# 문제점: 다이나믹 프로그래밍으로 접근하는 것에 비해 효율성 차이가 심하게 난다.

n = int(input())
# 창고의 식량 수를 창고의 인덱스와 함께 묶어서 리스트로 만듬
supplies = list(enumerate(map(int, input().split())))

# 식량 수를 기준으로 내림차순 정렬
supplies_sorted = sorted(supplies, key=lambda x: x[1], reverse=True)
visited = [False] * n  # 식량창고 방문 확인을 위한 리스트 초기화
result = 0  # 식량의 최댓값

# 가장 많은 식량을 가지고 있는 창고부터 확인
for s in supplies_sorted:
    idx = s[0]  # 창고의 인덱스 확인
    # 방문하지 않은 창고이고 해당 창고 좌우 창고도 방문하지 않은 상태라면
    if not visited[idx] and ((idx >= 1 and idx < n - 1 and not visited[idx - 1] and not visited[idx + 1]) or (idx == 0 and not visited[idx + 1]) or (idx == n - 1 and not visited[idx - 1])):
        visited[idx] = True  # 창고를 방문
        result += s[1]  # 식량 약탈

print(result)

# 모범 답안
# n = int(input())
# array = list(map(int, input().split()))
#
# d = [0] * 100  # DP 테이블 초기화
#
# # 다이나믹 프로그래밍 진행 (바텀업)
# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])
#
# print(d[n - 1])
