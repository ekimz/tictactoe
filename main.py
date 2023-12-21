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

# the keys will change depending on the moves that are made
board_keys = []

# this is to continuously add the roles that occur
for key in main_board:
    board_keys.append(key)


# we are defining the bizual effex of the tic-tac-toe game
def board_visual(board):
    print('     A   B   C')  # this is for reference to the columns
    print('    === === ===')
    print('1  :  ' + board['1A'] + ' | ' + board['1B'] + ' | ' + board['1C'])  # and reference to rows
    print('   : ---+---+---')
    print('2  :  ' + board['2A'] + ' | ' + board['2B'] + ' | ' + board['2C'])
    print('   : ---+---+---')
    print('3  :  ' + board['3A'] + ' | ' + board['3B'] + ' | ' + board['3C'])


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
    player_one.role = random.randint(1, 12)

    print('You just rolled a ' + str(player_one.role) + '! Good job, ' + player_one.name + '!')
    print('Let\'s see how you do, ' + player_two.name + '.')
    print(player_two.name + ', please say anything to throw your dice.')
    input()

    # generate random number and assign to role for player 1
    player_two.role = random.randint(1, 12)
    print('You just rolled a ' + str(player_two.role) + '! Great going, ' + player_two.name + '!')


def pick_role(player_one, player_two):
    winner = ''
    loser = ''

    if player_one.role > player_two.role:
        winner = player_one
        loser = player_two
    elif player_one.role < player_two.role:
        winner = player_two
        loser = player_one
    else:
        print('I see we have a tie! Let\'s try that again, shall we?')
        throw_dice(player_one, player_two)

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
        # tic_tac_toe(winner)

    else:
        winner.role = 'O'
        loser.role = 'X'
        print('Okay! It\'s decided: ' + winner.name + ' will be O, and ' + loser.name + ' will be X.')
        print(loser.name + ', since you are X, you will commence the game. No pressure...')
        # tic_tac_toe(loser)


def tic_tac_toe(player_one, player_two, board):
    player_role = 'X'  # The game will always start with 'X', so no need to associate with variable

    if player_one.role == 'X':
        player_x = player_one
        player_o = player_two
    else:
        player_x = player_one
        player_o = player_two

    for i in range(9):
        board_visual(board)  # show the board since we're visual creatures
        if player_role == 'X':
            print('Gotta catch \'em all, ' + player_x.name + ', put down your ' + player_x.role + '!')
        else:
            print('Gotta catch \'em all, ' + player_o.name + ', put down your ' + player_o.role + '!')

        # this is for adding any moves since from here on out they're just gonna be making moves
        move = input()  # 1A, 1B, 1C, 2A, 2B, 2C, 3A, 3B, 3C

        # when the move is not any of these
        while move not in ('1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C'):
            print('Hey that\'s illegal! Give me a real move.')
            move = input()

        else:
            # you can move to a spot that has NOT been filled
            if board[move] == ' ':
                board[move] = player_role
            elif board[move] == 'X' or board[move] == 'O':  # you can't move there since it's been filled
                print('You wish you could move there. Give it another shot.')
            else:
                print('That\'s not a real move. Once more, with vigor.')  # invalid move

        # if someone has won, you gotta give the celebratory speech
        victory = did_they_win_though(board)

        if victory == 1:
            print('It\'s over pufferfish, ' + player_x.name + ' wins this time!')  # yay, there's a winner!
        elif victory == 2:
            print('It\'s over pufferfish, ' + player_o.name + ' wins this time!')
        elif victory == 3:
            print('ESH, but there can always be another game.. jk... unless...?')  # if nobody wins, it's a tie
        else:
            if player_role == 'X':
                player_role = 'O'
            else:
                player_role = 'X'


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
    elif (board['1A'] == board['1B'] == board['1C'] != ' ') or \
            (board['2A'] == board['2B'] == board['2C'] != ' ') or \
            (board['3A'] == board['3B'] == board['3C'] != ' ') or \
            (board['1A'] == board['2A'] == board['3A'] != ' ') or \
            (board['1B'] == board['2B'] == board['3B'] != ' ') or \
            (board['1C'] == board['2C'] == board['3C'] != ' ') or \
            (board['1A'] == board['2B'] == board['3C'] != ' ') or \
            (board['3A'] == board['2B'] == board['1C'] != ' '):
        idk_you_tell_me = 3
    return idk_you_tell_me


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
    pick_role(player_1, player_2)

    # The logic of the game itself:
    print('We\'re ready to rumble!! ')
    tic_tac_toe(player_1, player_2, main_board)

    # you gotta take roles doing this thing
    # player one takes a role, and then player two
    # after someone puts down


# we need to define a player taking a role on the board, takes player and board move


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game_play()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
