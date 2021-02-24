# 내 풀이
while True:
    n = input()
    # 입력받은 문자열이 '0'이면 루프를 벗어남
    if n == '0':
        break
    # 입력받은 문자열과 그 문자열을 거꾸로 한 것을 비교
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
