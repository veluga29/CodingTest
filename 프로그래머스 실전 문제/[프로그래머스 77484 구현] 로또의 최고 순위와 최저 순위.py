# 내 풀이
# Time complexity: O(1)
# 만일 주어진 번호가 6개 고정이 아니라 n개였다면 O(n²)
# Space complexity: O(1)
def solution(lottos, win_nums):
    prize = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    
    zero_cnt = 0
    correct_cnt = 0
    for num in lottos:
        if num == 0:
            zero_cnt += 1
            continue
        if num in win_nums:
            correct_cnt += 1
    
    max_prev = correct_cnt + zero_cnt
    max_cnt = 6 if max_prev > 6 else max_prev
    min_cnt = correct_cnt
    
    return [prize[max_cnt], prize[min_cnt]]