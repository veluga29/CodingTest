# 내 풀이
# Time complexity: O(1)
# 만일 배열 숫자의 개수가 n개라면 O(n²)
# Space complexity: O(1)

def solution(numbers):
    answer = 0
    numbers = set(numbers) # set을 통한 in 연산이 조금 더 빠를 것이라 생각
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

# 모범 답안 1 - 값을 인덱스로 사용하는 방법 기억하자!
# Time complexity: O(n)
# def solution(numbers):
#     answer = 0
#     flags = [False] * 10
#     for number in numbers:
#         flags[number] = True
#     for i, flag in enumerate(flags):
#         if not flag:
#             answer += i
#     return answer

# 모범 답안 2
# def solution(numbers):
#     return 45 - sum(numbers)