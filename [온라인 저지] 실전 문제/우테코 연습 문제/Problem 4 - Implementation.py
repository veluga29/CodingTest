# 내 풀이
def solution(number):
    result = 0  # 손뼉을 치는 횟수
    for num in range(1, number + 1):
        digits = list(map(int, str(num)))  # 해당 숫자의 각 자리수를 리스트에 나눠 담음
        for i in digits:
            #  리스트 원소가 3, 6, 9에 해당한다면
            if i == 3 or i == 6 or i == 9:
                result += 1  # 손뼉 치기

    return result


print(solution(13))
print(solution(33))
