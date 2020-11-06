from functools import reduce


def solution(pobi, crong):
    # pobi나 crong이 펼친 페이지수가 홀, 짝 순으로 연속되어 있지 않으면 -1 return
    if pobi[1] != pobi[0] + 1 or crong[1] != crong[0] + 1 or (
            pobi[0] % 2 != 1 or pobi[1] % 2 != 0 or crong[0] % 2 != 1 or crong[1] % 2 != 0):
        return -1

    pobi_nums = []  # pobi의 각 페이지의 자리수를 담을 배열
    crong_nums = []  # crong의 각 페이지의 자리수를 담을 배열
    # pobi와 crong의 각 페이지마다 자리수를 나눠 리스트화해 pobi_nums, crong_nums에 저장
    for page in range(2):
        pobi_nums.append(list(map(int, str(pobi[page]))))
        crong_nums.append(list(map(int, str(crong[page]))))

    # pobi의 왼쪽 및 오른쪽 페이지 각각의 덧셈 값과 곱셈값을 구해, 그 중 최댓값을 구함
    l_plus, r_plus = map(sum, pobi_nums)
    l_mul = reduce(lambda x, y: x * y, pobi_nums[0])
    r_mul = reduce(lambda x, y: x * y, pobi_nums[1])
    pobi_max = max(l_plus, r_plus, l_mul, r_mul)

    # crong의 왼쪽 및 오른쪽 페이지 각각의 덧셈 값과 곱셈값을 구해, 그 중 최댓값을 구함
    l_plus, r_plus = map(sum, crong_nums)
    l_mul = reduce(lambda x, y: x * y, crong_nums[0])
    r_mul = reduce(lambda x, y: x * y, crong_nums[1])
    crong_max = max(l_plus, r_plus, l_mul, r_mul)

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
