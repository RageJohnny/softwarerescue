from math import inf as infinity
from random import choice
from time import sleep
import os

# Setup the variabels
player_human = -1
player_computer = 1
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


# Implementation of decision who won the game
def decision(state):
    if wins(state, player_computer):
        score = 1
    elif wins(state, player_human):
        score = -1
    else:
        score = 0
    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state


# Implementation of "game_over"
def game_over(state):
    return wins(state, player_human) or wins(state, player_computer)


def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells


# Implementation to check if the move is valid
def valid_move(x, y):
    return [x, y] in empty_cells(board)


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False


# Implementation of the MiniMax-Algorithm
def minimax(state, depth, player):
    if player == player_computer:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = decision(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == player_computer:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best


# Clean the shell for a better view
def clean():
    os.system('cls')


# Method for creating the game-board
def render(state, c_choice, h_choice):
    for row in state:
        print('\n----------------')
        for cell in row:
            if cell == player_computer:
                print('|', c_choice, '|', end='')
            elif cell == player_human:
                print('|', h_choice, '|', end='')
            else:
                print('|', ' ', '|', end='')
    print('\n----------------')


# Implementation of the AI-Turn using the MiniMax Algorithm
def ai_turn(c_choice, h_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, player_computer)
        x, y = move[0], move[1]

    set_move(x, y, player_computer)
    sleep(1)


# Implementation of the human turn
def human_turn(computer_choice, human_choice):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Compute a dictionary with all possible moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    render(board, computer_choice, human_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Zahl 1 - 9 eingeben bitte! '))
            coord = moves[move]
            move_try = set_move(coord[0], coord[1], player_human)

            if not move_try:
                print('FEHLER! FEHLER! NICHT MÖGLICH!')
                move = -1
        except KeyboardInterrupt:
            print('Bis zum nächsten Mal!')
            exit()
        except:
            print('FEHLER! FEHLER! NICHT MÖGLICH!')


def main():
    clean()
    choice_human = ''
    choice_computer = ''
    first = ''

    # Human chooses X or O to play
    while choice_human != 'O' and choice_human != 'X':
        try:
            print('')
            choice_human = input('Bitte X oder O auswählen!\nAuswahl: ').upper()
        except KeyboardInterrupt:
            print('Bis zum nächsten Mal!')
            exit()
        except:
            print('FEHLER! FEHLER! NICHT MÖGLICH!')

    # Setting computer's choice
    if choice_human == 'X':
        choice_computer = 'O'
    else:
        choice_computer = 'X'

    # Let the human decide if he wants to start first or not
    clean()
    while first != 'J' and first != 'N':
        try:
            first = input('Willst du den ersten Zug machen? [J/N]: ').upper()
        except KeyboardInterrupt:
            print('Bis zum nächsten Mal!')
            exit()
        except:
            print('FEHLER! FEHLER! NICHT MÖGLICH!')

    # Main game loop
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(choice_computer, choice_human)
            first = ''

        human_turn(choice_computer, choice_human)
        ai_turn(choice_computer, choice_human)

    # Game over message
    if wins(board, player_human):
        clean()
        print('Zeit zu denken... [{}]'.format(choice_human))
        render(board, choice_computer, choice_human)
        print('DU HAST GEWONNEN!')
    elif wins(board, player_computer):
        clean()
        print('Computer denkt... [{}]'.format(choice_computer))
        render(board, choice_computer, choice_human)
        print('DER COMPUTER HAT GEWONNEN!')
    else:
        clean()
        render(board, choice_computer, choice_human)
        print('UNENTSCHIEDEN!')

    exit()


if __name__ == '__main__':
    main()
