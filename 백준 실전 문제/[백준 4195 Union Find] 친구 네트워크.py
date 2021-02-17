# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 시간초과, 출력초과에 계속 걸려 시간을 많이 보냈는데,
# 개수를 세는 테이블을 따로 생성하고 같은 집합일 경우에는 합치기 연산을 중복으로 수행하지 않도록 예외처리하니 잘 풀렸다.

import sys
input = sys.stdin.readline


# 원소가 속한 집합의 루트 노드를 찾는 함수 정의
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치는 함수 정의
def union_parent(parent, cnt, a , b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        cnt[a] += cnt[b]  # 루트 노드에 전체 원소 개수 기록
    elif a > b:
        parent[a] = b
        cnt[b] += cnt[a]  # 루트 노드에 전체 원소 개수 기록


t = int(input())
for _ in range(t):
    f = int(input())
    # 부모 테이블과 네트워크 원소 개수를 세는 테이블을 딕셔너리로 생성
    parent = dict()
    cnt = dict()
    for _ in range(f):
        a, b = input().split()
        # 테이블에 없는 원소라면 초기화
        if a not in parent:
            parent[a] = a
            cnt[a] = 1
        if b not in parent:
            parent[b] = b
            cnt[b] = 1
        # union 연산 수행
        union_parent(parent, cnt, a, b)
        # 결과 출력
        print(cnt[find_parent(parent, a)])
