# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 아직도 완전히 이해는 안가지만 일단 넘어가자. LIS의 응용 문제이지 않을까 생각했는데, 다음에 다시 풀 때 아이디어가 바로 떠오를 것 같진 않다.
str1 = input()
str2 = input()

dp = [[0] * 1001 for _ in range(1001)]

# 최장 공통 부분 수열(LCS) 찾기
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:  # 가장 최근에 추가된 글자가 서로 같을 때
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:  # 추가된 글자가 서로 다를 때
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 결과 출력
print(dp[len(str1)][len(str2)])
