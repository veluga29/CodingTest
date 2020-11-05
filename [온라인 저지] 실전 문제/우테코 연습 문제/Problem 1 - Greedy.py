values = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]


def solution(money):
    result = [0] * 9
    global values

    for idx, value in enumerate(values):
        result[idx] += money // value
        money %= value

    return result


print(solution(50237))
print(solution(15000))
