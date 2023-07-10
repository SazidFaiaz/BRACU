def print_matrix(m):
  row , col = m.shape
  for i in range(row):
    co = 1
    print("|" , end = '')
    for j in range(col):
      co += 1
      if len(str(m[i][j])) == 1:
        print('', m[j][i], end='|')
        co += 6
      else:
        print(" ", m[i][j], end = '|')
        c += 6
    print()

    print('-' * (co -col))

def show_knight_move(knight):
  board = np.zeros((8,8), dtype = int)
  row , col = knight


  moves = [(2, 1), (2, -1),(-2, 1), (-2, -1),(1, 2), (-1, 2),(1, -2), (-1, -2)]

  for move in moves:
      move_row, move_col = move
      new_row = row + move_row
      new_col = col + move_col

      if 0 <= new_row < 8 and 0 <= new_col < 8:
          board[new_row][new_col] = 3

  board[row][col] = 33

  return board


knight = (3,4)
chess_board = show_knight_move(knight)
print_matrix(chess_board)
