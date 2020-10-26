# 수정 답안
n = int(input())
houses = list(map(int, input().split()))

houses.sort()

median = houses[(n - 1) // 2]  # 중간 값 구하기
print(median)

# 내 풀이 1 - 시간 초과
# n = int(input())
# houses = list(map(int, input().split()))

# houses.sort()
# distance = 10e5
# result = 0
#
# for i in houses:
#     tmp = 0  # 임시 비교값 설정
#     for j in houses:
#         tmp += abs(i - j)  # 안테나로부터 모든 집까지의 거리의 총합을 구함
#     if tmp < distance:  # 최소 거리 갱신
#         distance = tmp
#         result = i  # 최소 거리의 안테나 위치 저장

# print(result)

# 내 풀이 2 - 답이 틀림
# n = int(input())
# houses = list(map(int, input().split()))
#
# # 안테나로부터 모든 집까지의 거리의 총합과 안테나 위치를 튜플로 반환
# def order(x):
#     distance = 0
#     for i in houses:
#         distance += abs(x-i)
#     return (distance, x)
#
# # 집들을 안테나로부터 모든 집까지의 거리로 먼저 오름차순 정렬하고, 같다면 위치 값이 보다 작은 것을 먼저 오게 오름차순 정렬함
# houses.sort(key=order)
#
# print(houses[0])

