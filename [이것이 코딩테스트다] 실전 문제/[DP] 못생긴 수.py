# 내 풀이
# 문제점: 시간 복잡도는 문제 없을 것 같은데, 코드 depth가 깊다.
n = int(input())

dp = [0] * (n + 1)  # dp 테이블 생성
dp[1] = 1

# 다이나믹 프로그래밍 진행 (바텀업)
for i in range(2, n + 1):
    # 이전 못생긴 수 참조
    j = dp[i - 1]
    # 이전 못생긴 수의 다음 수부터 1개씩 차례대로 못생긴 수 탐색
    while True:
        j += 1
        j_tmp = j
        check = True  # 못생긴 수가 맞는지 체크
        while j_tmp != 1:
            if j_tmp % 2 == 0:
                j_tmp //= 2
            elif j_tmp % 3 == 0:
                j_tmp //= 3
            elif j_tmp % 5 == 0:
                j_tmp //= 5
            else:
                check = False
                break
        # 못생긴 수를 찾으면 i번째 못생긴 수로 기록
        if check:
            dp[i] = j
            break

print(dp[n])

# 모범 답안 - 아직 이해가 좀 안된다...
# n = int(input())
#
# ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
# ugly[0] = 1 # 첫 번째 못생긴 수는 1
#
# # 2배, 3배, 5배를 위한 인덱스
# i2 = i3 = i5 = 0
# # 처음에 곱셈 값을 초기화
# next2, next3, next5 = 2, 3, 5
#
# # 1부터 n까지의 못생긴 수들을 찾기
# for l in range(1, n):
#     # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
#     ugly[l] = min(next2, next3, next5)
#     # 인덱스에 따라서 곱셈 결과를 증가
#     if ugly[l] == next2:
#         i2 += 1
#         next2 = ugly[i2] * 2
#     if ugly[l] == next3:
#         i3 += 1
#         next3 = ugly[i3] * 3
#     if ugly[l] == next5:
#         i5 += 1
#         next5 = ugly[i5] * 5
#
# # n번째 못생긴 수를 출력
# print(ugly[n - 1])
