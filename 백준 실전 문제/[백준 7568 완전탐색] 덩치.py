# 내 풀이 - 문제 풀이 실패, 수정 답안
# 생각해볼 점: 처음엔 입력 수가 많지 않아 조건에 맞춰 bubble sort를 한 후, 정렬된 정보대로 차례차례 비교하며 등수를 출력해보면 어떨까 했다.
# 그런데 무언가 깔끔한 느낌이 없는 것 같아 다른 풀이를 찾아보니, 굳이 정렬할 필요없이 완전탐색으로 전부 비교하며 접근하는 것이 현명했던 것 같다.
# 시간 복잡도: O(N²) - n이 최대 50이라 큰 문제 없었음

n = int(input())
# 사람들의 덩치 정보 입력 받기
people = [tuple(map(int, input().split())) for _ in range(n)]

# 현재 사람의 덩치를 다른 모든 사람들과 비교하여
for i in range(n):
    rank = 1
    # 만일 현재 사람보다 덩치가 큰 사람이 있다면, rank를 1 증가시킴
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    # 현재 사람의 등수 출력
    print(rank, end=' ')
