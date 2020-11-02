# 내 풀이
def solution(board, moves):
    answer = 0
    basket = []  # 바구니를 리스트로 구현해 스택으로 사용

    # 크레인을 작동시킨 위치 확인
    for move in moves:
        # 크레인을 작동해 인형이 있는지 확인
        for i in range(len(board)):
            # 인형이 있다면, 뽑아서 바구니에 넣음
            if board[i][move - 1] != 0:
                basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
        # 바구니에 연속한 두 개의 인형이 있다면 터트리고, 터트린 인형의 숫자를 셈
        if len(basket) > 1 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2

    return answer