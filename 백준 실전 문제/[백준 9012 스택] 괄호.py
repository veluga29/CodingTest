t = int(input())  # 테스트 케이스 개수 저장

# 각 테스트 케이스에 대하여 알고리즘 수행
for num in range(t):
    ps = list(input())
    stack = [ps.pop(0)]  # 스택을 만들어 입력의 첫번째 괄호를 담음
    for p in ps:
        # 스택에 괄호가 존재하며, 최상단에 있는 괄호가 '('이고 새로 스택에 들어오는 괄호가 ')'라면
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()  # 스택의 최상단 괄호 제거
        # 다른 경우 스택에 새로운 괄호를 삽입
        else:
            stack.append(p)
    # 스택에 괄호가 남아있을 경우
    if stack:
        print("NO")
    # 스택이 비어 있을 경우
    else:
        print("YES")
