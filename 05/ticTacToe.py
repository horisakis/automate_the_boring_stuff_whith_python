the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
  print('-+-+-')

turn = 'x'
for i in range(9):
  print_board(the_board)
  print(turn + 'の順番です。どこに打つ？')
  move = input()
  the_board[move] = turn
  if turn == 'x':
    turn = 'o'
  else:
    turn = 'x'    
print_board(the_board)
