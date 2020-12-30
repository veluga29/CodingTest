while True:
    string = input()
    # '.'이 입력되면 종료
    if string == '.':
        break
    stack = []
    for s in string:
        # 스택에 괄호가 존재할 때, 최상단이 '('이면서 ')'이 입력이거나 최상단이 '['이면서 ']'이 입력되는 경우
        if stack and ((stack[-1] == '(' and s == ')') or (stack[-1] == '[' and s == ']')):
            stack.pop()  # 스택의 최상단 괄호를 제거
        # 위 경우가 아닐 때 s가 ()[]중 하나인 경우 스택에 삽입
        elif s in "([)]":
            stack.append(s)

    if stack:
        print("no")
    else:
        print("yes")
