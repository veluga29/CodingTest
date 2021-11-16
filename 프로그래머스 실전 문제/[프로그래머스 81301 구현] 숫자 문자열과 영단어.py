# 내 풀이
# s의 길이 = n
# Time complexity: O(n)
# Space complexity: O(n)
from collections import deque

def solution(s):
    num_and_tail_cnt_dict = {
        'ze': ['0', 2],
        'on': ['1', 1],
        'tw': ['2', 1],
        'th': ['3', 3],
        'fo': ['4', 2],
        'fi': ['5', 2],
        'si': ['6', 1],
        'se': ['7', 3],
        'ei': ['8', 3],
        'ni': ['9', 2]
    }   
    
    answer = ''
    s_queue = deque(list(s))
    
    while s_queue:
        first_c = s_queue.popleft()
        # 숫자일 때 - 보다 파이썬스러운 방법: first_c.isdigit()
        if ord(first_c) >= 48 and ord(first_c) <= 57: 
            answer += first_c
            continue
        # 문자일 때
        # 두 번째 글자까지 확인
        second_c = s_queue.popleft()
        word_head = first_c + second_c
        num, tail_cnt = num_and_tail_cnt_dict[word_head]
        answer += num
        for _ in range(tail_cnt):
            s_queue.popleft()
            
    return int(answer)

# 다른 풀이 - cursor의 활용법과 * 10으로 숫자를 잇는 것이 Point!
# def solution(s):
#     cursor = 0
#     answer = 0
#     while cursor < len(s):
#         if s[cursor].isdigit():
#             answer = answer * 10 + int(s[cursor])
#             cursor += 1
#         elif s[cursor] == 'z': # zero
#             answer = answer * 10
#             cursor += 4
#         elif s[cursor] == 'o': #one or four    
#             answer = answer * 10 + 1
#             cursor += 3
#         elif s[cursor] == 't': #two or three
#             if s[cursor+1] == 'w': #two
#                 answer = answer * 10 + 2
#                 cursor += 3
#             else: #three
#                 answer = answer * 10 + 3
#                 cursor += 5
#         elif s[cursor] == 'f': #four or five
#             if s[cursor+1] == 'o': #four
#                 answer = answer * 10 + 4
#                 cursor += 4
#             else:
#                 answer = answer * 10 + 5
#                 cursor += 4
#         elif s[cursor] == 's': #six or seven
#             if s[cursor+1] == 'i': #six
#                 answer = answer * 10 + 6
#                 cursor += 3
#             else: #seven
#                 answer = answer * 10 + 7
#                 cursor += 5
#         elif s[cursor] == 'e':
#             answer = answer * 10 + 8
#             cursor += 5
#         elif s[cursor] == 'n': 
#             answer = answer * 10 + 9
#             cursor += 4
#     return answer