# 내 풀이
import sys
input = sys.stdin.readline

# 주어진 정보 입력 받기
n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]  # 그래프 연결 상태 입력 받기
plan = list(map(int, input().split()))  # 여행 계획 입력 받기

# 부모 테이블 생성 및 초기화
parent = [i for i in range(n + 1)]


# 특정 원소가 속한 집합을 찾아주는 Find 연산 정의
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합쳐주는 Union 연산 정의
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 그래프 연결 상태를 확인하여 Union 연산 수행
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

plan_flag = True  # 여행 계획 가능 여부 체크

# 두 원소가 같은 집합인지 확인하여 여행 계획 가능 여부 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        plan_flag = False
        break

# 결과 출력
if plan_flag:
    print("YES")
else:
    print("NO")
