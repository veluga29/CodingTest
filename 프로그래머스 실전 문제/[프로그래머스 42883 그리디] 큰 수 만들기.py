# 내 풀이
# 문제점: 테스트 케이스에 따라 처리속도가 오래 걸린다.
# 개선할 점: 스택의 도입으로 알고리즘을 훨씬 효율적으로 처리할 수 있다.


def solution(number, k):
    answer = ''
    idx = 0  # 매 단계에서 가장 큰 숫자의 인덱스
    while k > 0:  # 제거할 것이 있을 때까지
        max_val = '-1'
        start_idx = idx  # 이번 단계의 시작 인덱스를 기록
        # 시작 인덱스부터 뒤로 k + 1개 만큼 탐색하여 가장 큰 수 찾음
        for i in range(idx, idx + k + 1):
            if eval(number[i] + '>' + max_val):
                max_val = number[i]
                idx = i
            # 만일 찾은 수가 9라면 뒷 부분은 더 탐색하지 않고 루프 종료
            if max_val == '9':
                break
        answer += number[idx]
        k -= idx - start_idx  # 이번 단계에 제거한 숫자의 개수를 차감
        idx += 1
        # 만일 제거할 개수가 남았는데 가장 큰 숫자를 얻었다면, 그대로 리턴
        if len(answer) + k == len(number):
            return answer

    answer += number[idx:]  # 제거가 끝난 후, 아직 체크하지 않은 남은 뒷부분을 답에 추가
    return answer

# 지향할 답안
# def solution(number, k):
#     stack = [number[0]]
#     for num in number[1:]:
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(num)
#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)
