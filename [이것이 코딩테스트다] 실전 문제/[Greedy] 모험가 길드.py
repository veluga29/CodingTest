# 내 풀이
# 고려할 점 : 좀 더 로직이 깔끔하게 눈에 들어오게 짜면 좋겠다.

n = int(input())
guild = list(map(int, input().split()))

# 낮은 공포도 순으로 정렬
guild.sort()

result = 0  # 여행을 떠날 그룹의 수
i = 0  # 인덱스

# j를 하나씩 올리면서 인덱스를 이용해 그룹 숫자 카운트
for j in range(n):
    # j번째 모험가의 공포도가 (j - i + 1)명의 모험가 수와 같을 때, 그룹을 하나 만듬
    if guild[j] == j - i + 1:
        result += 1  # 그룹의 수 카운트
        i = j + 1  # i를 (j+1) 번째 모험가를 가리키도록 옮김

print(result)

# 지향할 답안
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수
#
# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
#
# print(result) # 총 그룹의 수 출력
