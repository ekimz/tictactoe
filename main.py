# a game of tic-tac-toe

# Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
# The program should let the players take roles to input their moves.
# The program should report the outcome of the game.

# During your interview, you will pair on adding support for a computer player to your game.
# You can start with random moves and make the AI smarter if you have time.


# I saw an implementation with a dictionary that I really liked, so we're gonna start there
main_board = {'1A': ' ', '1B': ' ', '1C': ' ',  # rows are 1, 2, 3
              '2A': ' ', '2B': ' ', '2C': ' ',  # cols are A, B, C
              '3A': ' ', '3B': ' ', '3C': ' '}


def clear_board(board):
    for key in board.keys():
        board[key] = ' '


# we are defining the bizual effex of the tic-tac-toe game
def board_visual(board):
    print('    A   B   C')  # this is for reference to the columns
    print('  :=== === ===:')
    print('1 : ' + board['1A'] + ' | ' + board['1B'] + ' | ' + board['1C'] + ' :')  # and reference to rows
    print('  :---+---+---:')
    print('2 : ' + board['2A'] + ' | ' + board['2B'] + ' | ' + board['2C'] + ' :')
    print('  :---+---+---:')
    print('3 : ' + board['3A'] + ' | ' + board['3B'] + ' | ' + board['3C'] + ' :')
    print('  :=== === ===:')


def winning_visual(board):
    print('✩*⋆｡*      A   B   C    *｡⋆*✩')  # this is for reference to the columns
    print('*｡⋆*✩    :=== === ===:  ✩*⋆｡*')
    print(
        '✩*⋆｡*  1 : ' + board['1A'] + ' | ' + board['1B'] + ' | ' + board['1C'] + ' :  *｡⋆*✩')  # and reference to rows
    print('*｡⋆*✩    :---+---+---:  ✩*⋆｡*')
    print('✩*⋆｡*  2 : ' + board['2A'] + ' | ' + board['2B'] + ' | ' + board['2C'] + ' :  *｡⋆*✩')
    print('*｡⋆*✩    :---+---+---:  ✩*⋆｡*')
    print('✩*⋆｡*  3 : ' + board['3A'] + ' | ' + board['3B'] + ' | ' + board['3C'] + ' :  *｡⋆*✩')
    print('*｡⋆*✩    :=== === ===:  ✩*⋆｡*')


# well I still want players, so we have to add that
class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def throw_dice(player_one, player_two):
    import random
    print(player_one.name + ', please say anything to throw your dice.')
    input()

    # generate random number and assign to role for player 1
    player_one.role = random.randint(1, 6) + random.randint(1, 6)

    print('You just rolled a ' + str(player_one.role) + '! Good job, ' + player_one.name + '!')
    print('Let\'s see how you do, ' + player_two.name + '.')
    print(player_two.name + ', please say anything to throw your dice.')
    input()

    # generate random number and assign to role for player 1
    player_two.role = random.randint(1, 6) + random.randint(1, 6)
    print('You just rolled a ' + str(player_two.role) + '! Great going, ' + player_two.name + '!')

    if player_one.role != player_two.role:
        pick_role(player_one, player_two)
    else:
        throw_dice(player_one, player_two)


def pick_role(player_one, player_two):
    if player_one.role > player_two.role:
        winner = player_one
        loser = player_two
    elif player_one.role < player_two.role:
        winner = player_two
        loser = player_one

    print(winner.name + ' won! Now you can decide: Would you like to be X or O?')
    chosen_role = input()
    while chosen_role != 'X' and chosen_role != 'O':
        print('We\'re picky, please provide an X or an O.')
        chosen_role = input()

    if chosen_role == 'X':
        winner.role = 'X'
        loser.role = 'O'
        print('Okay! It\'s decided: ' + winner.name + ' will be X, and ' + loser.name + ' will be O.')
        print(winner.name + ', since you are X, you will start the game. Good luck!')

    else:
        winner.role = 'O'
        loser.role = 'X'
        print('Okay! It\'s decided: ' + winner.name + ' will be O, and ' + loser.name + ' will be X.')
        print(loser.name + ', since you are X, you will commence the game. No pressure...')


def tic_tac_toe(player_one, player_two, board):
    player_role = 'X'  # The game will always start with 'X', so no need to associate with variable
    victory = 0

    if player_one.role == 'X':
        player_x = player_one
        player_o = player_two
    else:
        player_x = player_two
        player_o = player_one

    while victory == 0:
        board_visual(board)  # show the board since we're visual creatures
        print('\n')
        if player_role == 'X':
            print('Gotta catch \'em all, ' + player_x.name + ', put down your ' + player_x.role + '!')
        else:
            print('Gotta catch \'em all, ' + player_o.name + ', put down your ' + player_o.role + '!')

        # this is for adding any moves since from here on out they're just gonna be making moves
        all_the_right_moves(board, player_role)

        # if someone has won, you gotta give the celebratory speech
        victory = did_they_win_though(board)  # grab the check to see if someone won

        if victory == 1:
            winning_visual(board)
            print('\n')
            print('It\'s over pufferfish, ' + player_x.name + ' wins this time!')  # yay, there's a winner!
            play_again(player_one, player_two, board)

        elif victory == 2:
            winning_visual(board)
            print('\n')
            print('It\'s over pufferfish, ' + player_o.name + ' wins this time!')
            play_again(player_one, player_two, board)

        elif victory == 3:
            board_visual(board)
            print('\n')
            print('ESH, but there can always be another game.. jk... unless...?')  # if nobody wins, it's a tie
            play_again(player_one, player_two, board)

        else:
            if player_role == 'X':
                player_role = 'O'
            else:
                player_role = 'X'


def all_the_right_moves(board, player_role):
    # define the move as what you get
    move = input()

    while move in ('1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C'):
        if board[move] == ' ':
            board[move] = player_role
            break
        else:
            if board[move] == 'X' or board[move] == 'O':  # you can't move there since it's been filled
                print('You wish you could move there. Give it another shot.')
                move = input()
            else:
                print('That\'s not a real move. Once more, with vigor.')  # invalid move
                move = input()
    else:
        print('Hey that\'s illegal! Give me a real move.')
        all_the_right_moves(board, player_role)


def did_they_win_though(board):
    idk_you_tell_me = 0
    if (board['1A'] == board['1B'] == board['1C'] == 'X') or \
            (board['2A'] == board['2B'] == board['2C'] == 'X') or \
            (board['3A'] == board['3B'] == board['3C'] == 'X') or \
            (board['1A'] == board['2A'] == board['3A'] == 'X') or \
            (board['1B'] == board['2B'] == board['3B'] == 'X') or \
            (board['1C'] == board['2C'] == board['3C'] == 'X') or \
            (board['1A'] == board['2B'] == board['3C'] == 'X') or \
            (board['3A'] == board['2B'] == board['1C'] == 'X'):
        idk_you_tell_me = 1
    elif (board['1A'] == board['1B'] == board['1C'] == 'O') or \
            (board['2A'] == board['2B'] == board['2C'] == 'O') or \
            (board['3A'] == board['3B'] == board['3C'] == 'O') or \
            (board['1A'] == board['2A'] == board['3A'] == 'O') or \
            (board['1B'] == board['2B'] == board['3B'] == 'O') or \
            (board['1C'] == board['2C'] == board['3C'] == 'O') or \
            (board['1A'] == board['2B'] == board['3C'] == 'O') or \
            (board['3A'] == board['2B'] == board['1C'] == 'O'):
        idk_you_tell_me = 2
    elif all( board[key] != ' ' for key in board.keys()):
        idk_you_tell_me = 3
    return idk_you_tell_me


def play_again(player_one, player_two, board):
    print('Would you like to play another round? Y/N')
    answer = input()

    # if they're just keyboard mashing
    while answer != 'Y' and answer != 'N':
        print('It\'s a yes or no question, help a robot out. Y/N?')
        answer = input()
    else:
        if answer == 'Y':  # Yay they want to play again! Good job team!
            clear_board(board)
            tic_tac_toe(player_one, player_two, board)
        elif answer == 'N':  # It's okay they have things to do!
            print('Thanks for playing! See you next time~')


def game_play():
    # Little intro
    print('Welcome to a game of tic-tac-toe!')
    print('Let\'s get you situated, Player 1 and Player 2.')
    print('Player 1, what is your name?')

    # first allow player 1 to input their name
    player_1 = Player(input(), role='')
    print('Nice to meet you ' + player_1.name + '!')

    # allow player 2 to input their name also
    print('And Player 2, how about you?')
    player_2 = Player(input(), role='')
    print('Great to meet you, ' + player_2.name + '!')

    print('Now let\'s get started, shall we?')

    print('To begin this wretched game of tic tac toe, you will throw some elbo--I mean dice.')
    throw_dice(player_1, player_2)

    # The logic of the game itself:
    print('We\'re ready to rumble!! ')
    tic_tac_toe(player_1, player_2, main_board)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_play()
