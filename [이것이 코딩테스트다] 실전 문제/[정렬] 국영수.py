# 내 풀이 - 문제 풀이 실패, 수정 답안
# 주목할 점 : sort 메소드의 key 속성 활용법 학습

n = int(input())
info = [input().split() for _ in range(n)]  # 학생 정보 입력 받기

info.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름 출력
for student in info:
    print(student[0])
