# 내 풀이 - 시간초과, 수정 답안
# 문제점: 데이터 수가 최대 100,000개이므로 시간복잡도 O(NlogN)으로 해결해야 하지만, 원래의 내 풀이는 permutation으로 완전탐색하는 바람에 시간 초과를 만들었다.
# 주목할 점: 숫자가 1,000 이하라는 점을 보고 각 숫자를 문자열로 만들어 3을 곱하는 아이디어가 대단했다. 같은 자리수로 만들어 문자열끼리 비교하므로 인해 사전식 정렬이 가능해졌다.


def solution(numbers):
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)

    return str(int(''.join(map(str, numbers))))

# 원래의 내 풀이 - 완전 탐색으로 접근해 답은 맞으나 시간 초과
# from itertools import permutations
# def solution(numbers):
#     max_num = '0'  # 만들 수 있는 가장 큰 수 저장
#     # 만들 수 있는 모든 수를 순열로 확인
#     p_numbers = permutations(numbers, len(numbers))

#     # 모든 경우의 수를 문자열 상태로 비교하며 가장 큰 수 탐색
#     for p in p_numbers:
#         num = ''.join(map(str, p))
#         if eval(num + '>' + max_num):
#             max_num = num

#     return max_num