# 내 풀이
k = int(input())
stack = []  # 스택 생성
for i in range(k):
    n = int(input())
    # 입력되는 수가 0이면 최근 기록한 수 제거, 0이 아니면 입력된 수 기록
    stack.append(n) if n != 0 else stack.pop()

print(sum(stack))
