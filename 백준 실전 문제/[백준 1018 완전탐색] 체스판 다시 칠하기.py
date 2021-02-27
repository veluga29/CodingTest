def paint_board(chess_board):
    cnt_b, cnt_w = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess_board[i][j] == 'W':
                    cnt_b += 1
                if chess_board[i][j] == 'B':
                    cnt_w += 1
            if (i + j) % 2 != 0:
                if chess_board[i][j] == 'W':
                    cnt_b += 1
                if chess_board[i][j] == 'B':
                    cnt_w += 1
            chess_board[i][j]


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n - 7):
    for j in range(m - 7):
        chess_board = [row[j:j+8] for row in board[i:i+8]]
