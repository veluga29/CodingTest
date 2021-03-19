# 내 풀이
# 시간 복잡도: O(N)

n = int(input())
title = 666  # 영화 제목에 들어간 수
series = 1  # 해당 영화의 시리즈 순서

# n번째 영화를 찾을 때까지 완전 탐색
while series < n:
    # 숫자를 하나씩 늘려가며
    title += 1
    # 숫자에 '666'이 들어가면 영화 시리즈 개수로 셈
    if '666' in str(title):
        series += 1

# n번째 영화의 제목에 포함된 수 출력
print(title)
