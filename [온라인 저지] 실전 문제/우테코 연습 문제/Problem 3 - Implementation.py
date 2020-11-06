# 내 풀이
from functools import reduce


# 숫자를 각각의 자리수를 담은 배열로 리턴하는 함수
def make_nums(num):
    return [list(map(int, str(num[page]))) for page in range(2)]


# 왼쪽 및 오른쪽 페이지 각각의 덧셈 값과 곱셈값을 구해, 그 중 최댓값을 구하는 함수
def max_among_plus_mul(nums_array):
    l_plus, r_plus = map(sum, nums_array)
    l_mul = reduce(lambda x, y: x * y, nums_array[0])
    r_mul = reduce(lambda x, y: x * y, nums_array[1])

    return max(l_plus, r_plus, l_mul, r_mul)


def solution(pobi, crong):
    # pobi나 crong이 펼친 페이지수가 홀, 짝 순으로 연속되어 있지 않으면 -1 return
    if pobi[1] != pobi[0] + 1 or crong[1] != crong[0] + 1 or (
            pobi[0] % 2 != 1 or pobi[1] % 2 != 0 or crong[0] % 2 != 1 or crong[1] % 2 != 0):
        return -1

    # pobi와 crong의 각 페이지의 자리수를 담는 배열 구하기
    pobi_nums = make_nums(pobi)
    crong_nums = make_nums(crong)

    # pobi와 crong 각각의 최댓값 구하기
    pobi_max = max_among_plus_mul(pobi_nums)
    crong_max = max_among_plus_mul(crong_nums)

    if pobi_max > crong_max:  # pobi가 이겼다면
        answer = 1
    elif pobi_max < crong_max:  # crong이 이겼다면
        answer = 2
    elif pobi_max == crong_max:  # 서로 비겼다면
        answer = 0

    return answer


print(solution([97, 98], [197, 198]))
print(solution([131, 132], [211, 212]))
print(solution([99, 102], [211, 212]))
