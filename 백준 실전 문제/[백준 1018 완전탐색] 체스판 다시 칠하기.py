# 내 풀이


# 첫 칸을 검은색, 흰색 각각으로 칠할 때, 둘 중 다시 칠해야 하는 횟수가 최소인 값을 리턴하는 함수 정의
def paint_board(chess_board):
    # 첫 칸이 검은색일 경우와 흰색일 경우, 각각 다시 칠하는 횟수
    start_b, start_w = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess_board[i][j] != 'B':
                    start_b += 1
                if chess_board[i][j] != 'W':
                    start_w += 1
            else:
                if chess_board[i][j] != 'W':
                    start_b += 1
                if chess_board[i][j] != 'B':
                    start_w += 1
    min_val = min(start_b, start_w)

    return min_val


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]  # MN 보드 입력 받기
result = int(10e9)  # 다시 칠하는 최소 횟수

# 각각의 체스판 중 가장 최소인 값 탐색
for i in range(n - 7):
    for j in range(m - 7):
        # 8 X 8 체스판 크기로 보드를 slicing
        chess_board = [row[j:j+8] for row in board[i:i+8]]
        min_paint_cnt = paint_board(chess_board)
        # 현재 체스판의 값이 최소면, 최소값 갱신
        result = min(result, min_paint_cnt)

# 결과 출력
print(result)

