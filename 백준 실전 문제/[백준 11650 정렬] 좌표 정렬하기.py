# 내 풀이
n = int(input())
# 좌표를 (x, y) 튜플 형태로 리스트에 저장함
locations = [tuple(map(int, input().split())) for _ in range(n)]

# 주어진 조건대로 정렬 수행
locations.sort(key=lambda loc: (loc[0], loc[1]))

# 수행 결과 출력
for loc in locations:
    print(loc[0], loc[1])
