from random import randint

board = []
urn = 0

for x in range(5):
  board.append(["O"] * 10)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    if turn >= 3:
        print("Game Over")
        board[ship_row - 1][ship_col - 1] = "S"
        print_board(board)
        break
    else:
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            board[ship_row - 1][ship_col - 1] = "S"
            print_board(board)
            break
        else:
            if (guess_row < 1 or guess_row > len(board)) or (guess_col < 1 or guess_col > len(board) - 1):
              print("Oops, that's not even in the ocean.")
            elif board[guess_row - 1][guess_col - 1] == "X":
              print("You guessed that one already.")
              print_board(board)
            else:
              print("You missed my battleship!")
              board[guess_row - 1][guess_col - 1] = "X"
              print_board(board)
