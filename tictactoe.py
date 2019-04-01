def display_board(board):
    index_number = 0
    for item in range(1,4):
        print( '   |   |   ')
        print(f' {board[index_number]} | {board[index_number + 1]} | {board[index_number + 2]} ')
        if(item < 3):
            print('___|___|___')
        else:
            print( '   |   |   ')
        index_number+=3

game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


def player_input():
	inp = input(f'{name1} Do you want to be X ? Y|N ')
	inp = inp.upper()
	while inp.upper() != 'Y' and inp != 'N':
		print("Invalid input! Please try again")
		inp = input('Player 1: Do you want to be X or 0? Y|N ')
	return inp

def display_input(choice):
	if choice == 'Y':
		print(f'{name1} is X and will start first')
	else:
		print(f'{name2} is X and will start first')

def place_marker(board, marker, position):
	board[position - 1] = marker

def win_check(board, mark):
	i = 0
	if(board[i] == mark and board[i+1] == mark and board [i+2] == mark):
		return True

	if(board[i] == mark and board[i+3] == mark and board [i+6] == mark):
		return True

	if(board[i] == mark and board[i+4] == mark and board [i+8] == mark):
		return True

	i = 1
	if(board[i] == mark and board[i+3] == mark and board [i+6] == mark):
		return True

	i = 2
	if(board[i] == mark and board[i+3] == mark and board [i+6] == mark):
		return True
	if(board[i] == mark and board[i+2] == mark and board [i+4] == mark):
		return True


	i = 3
	if(board[i] == mark and board[i+1] == mark and board [i+2] == mark):
		return True

	i = 6
	if(board[i] == mark and board[i+1] == mark and board [i+2] == mark):
		return True

	return False

def space_check(board, position):

	if position < 1 and position > 9:
		return False
	if board[position - 1] == ' ':
		return True
	return False

def full_board_check(board):

	return " " in board

def player_choice(board):

	inp = int(input("What is your next position? "))
	return inp

def replay():
	inp = input("Do you want to play again? Y|N ")

print('Welcome to Tic Tac Toe')

name1 = input("Insert player 1 name ")

name2 = input("Insert player 2 name ")

display_board(game_board)

player1 = player_input()

display_input(player1)

firstplayer = ""

secondplayer = ""

if player1 == 'Y':
	firstplayer = name1
	secondplayer = name2

else:
	firstplayer = name2
	secondplayer = name1

ok = 1

while full_board_check(game_board) == True:

	print(f'It is {firstplayer} turn!')

	p = player_choice(game_board)

	while space_check(game_board, p) == False:

		print(f'{p} is not a free space.')

		p = player_choice(game_board)

	if ok == 1:

		place_marker(game_board, 'X', p)

		ok = 0

	else:
		place_marker(game_board, 'Y', p)
		ok = 1
	display_board(game_board)


	if win_check(game_board, 'X') == True:
		print(f'Congratulations, {firstplayer} won')
		break
	if win_check(game_board, 'Y') == True:
		print(f'Congratulations, {secondplayer} won')
		break
	firstplayer, secondplayer = secondplayer, firstplayer
input()

























