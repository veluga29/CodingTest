def solution(clothes):
    answer = 1
    # dictionary 형태로 재구성
    c_dict = {}
    for val, key in clothes:
        if key in c_dict.keys():
            c_dict[key].append(val)
        else:
            c_dict[key] = [val]
    # 안 입은 경우의 수를 포함해서 옷의 종류 별 개수들을 각각 곱함
    for val in c_dict.values():
        answer *= (len(val) + 1)

    return answer - 1  # 하나도 안 입은 경우의 수를 빼고 반환
