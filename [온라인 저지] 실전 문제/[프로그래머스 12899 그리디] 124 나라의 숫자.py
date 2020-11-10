# 내 풀이
def solution(n):
    answer = ''
    num = ['1', '2', '4']  # 124 나라의 수를 3진법의 0, 1, 2에 대응시킴

    while n:
        n -= 1  # 3진법에 124나라 숫자를 대응시키기위해 10진법 숫자에서 1을 뺌
        answer = num[n % 3] + answer
        n //= 3

    return answer
