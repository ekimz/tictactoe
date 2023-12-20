# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Before your interview, write a program that lets two humans play a game of Tic Tac Toe in a terminal.
# The program should let the players take turns to input their moves.
# The program should report the outcome of the game.

# During your interview, you will pair on adding support for a computer player to your game.
# You can start with random moves and make the AI smarter if you have time.


# I saw an implementation with a dictionary that I really liked so we're gonna start there
main_board = {'1A': ' ', '1B': ' ', '1C': ' ',  # rows are 1, 2, 3
              '2A': ' ', '2B': ' ', '2C': ' ',  # cols are A, B, C
              '3A': ' ', '3B': ' ', '3C': ' '}

# the keys will change depending on the moves that are made
board_keys = []

# this is to continuously add the turns that occur
for key in main_board:
    board_keys.append(key)


# we are defining the bizual effex of the tic tac toe game
def board_visual(board):
    print('  A B C')  # this is for reference to the columns
    print('1 ' + board['1A'] + '|' + board['1B'] + '|' + board['1C'])  # and reference to rows
    print(' --+-+--')
    print('2 ' + board['2A'] + '|' + board['2B'] + '|' + board['2C'])
    print(' --+-+--')
    print('3 ' + board['3A'] + '|' + board['3B'] + '|' + board['3C'])


# well I still want players so we have to add that

class Player:
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn


def throw_dice(player_one, player_two):
    import random
    print(player_one.name + ', please say anything to throw your dice.')
    input()

    # generate random number and assign to turn for player 1
    player_one.turn = random.randint(1, 12)

    print('You just rolled a ' + str(player_one.turn) + '! Good job, ' + player_one.name + '!')
    print('Let\'s see how you do, ' + player_two.name + '.')
    print(player_two.name + ', please say anything to throw your dice.')
    input()

    # generate random number and assign to turn for player 1
    player_two.turn = random.randint(1, 12)
    print('You just rolled a ' + str(player_two.turn) + '! Great going, ' + player_two.name + '!')


def pick_turn(player_one, player_two):
    if player_one.turn > player_two.turn:
        winner = player_one
        loser = player_two
    elif player_one.turn < player_two.turn:
        winner = player_two
        loser = player_one
    else:
        print('I see we have a tie! Let\'s try that again, shall we?')
        throw_dice()

    print(winner.name + ' won! Now you can decide: Would you like to be X or O?')
    chosen_turn = input()
    while chosen_turn != 'X' and chosen_turn != 'O':
        print('We\'re picky, please provide an X or an O.')
        chosen_turn = input()

    if chosen_turn == 'X':
        winner.turn = 'X'
        loser.turn = 'O'
        print('Okay! It\'s decided: ' + winner.name + ' will be X, and ' + loser.name + ' will be O.')
        print(winner.name + ', since you are X, you will start the game. Good luck!')
        tic_tac_toe(winner)

    else:
        winner.turn = 'O'
        loser.turn = 'X'
        print('Okay! It\'s decided: ' + winner.name + ' will be O, and ' + loser.name + ' will be X.')
        print(loser.name + ', since you are X, you will commence the game. No pressure...')
        tic_tac_toe(loser)


# def tic_tac_toe(ex, oh):

def did_they_win_though():
    if (main_board['1A'] == main_board['1B'] == main_board['1C'] != ' ') or  # win in the first row
        (main_board['2A'] == main_board['2B'] == main_board['2C'] != ' ') or  # second row
        (main_board['3A'] == main_board['3B'] == main_board['3C'] != ' ') or  # third row
        (main_board['1A'] == main_board['2A'] == main_board['3A'] != ' ') or  # first column
        (main_board['1B'] == main_board['2B'] == main_board['3B'] != ' ') or  # second column
        (main_board['1C'] == main_board['2C'] == main_board['3C'] != ' ') or  # third column
        (main_board['1A'] == main_board['2B'] == main_board['3C'] != ' ') or  # diagonal top left down
        (main_board['3A'] == main_board['2B'] == main_board['1C'] != ' '):  # diagonal bottom left up
        board_visual(main_board)  # show the board as evidence
        print('It\'s over pufferfish, ' + winner + ' wins this time!')  # whoever threw down that turn totally wins

    turn = 'X'  # just has to be one or the other
    count = 0  # started from the bottom now we're here

    for i in range(10):
        board_visual(main_board)
        print('Gotta catch \'em all, ' + player_1.name + ', make your move!')

        # this is for adding any moves since from here on out they're just gonna be making moves
        move = input()  # 1A, 1B, 1C, 2A, 2B, 2C, 3A, 3B, 3C

        # you can't move to a spot that's already filled
        if main_board[move] == ' ':
            main_board[move] = turn
            count += 1
        else:
            print('You can\'t move there. Try again.')
            continue







# okay and then I guess the main game play has to be written down somewhere or whatever


def game_play():
    # Little intro
    print('Welcome to a game of tic-tac-toe!')
    print('Let\'s get you situated, Player 1 and Player 2.')
    print('Player 1, what is your name?')

    # first allow player 1 to input their name
    player_1 = Player(input(), turn='')
    print('Nice to meet you ' + player_1.name + '!')

    # allow player 2 to input their name also
    print('And Player 2, how about you?')
    player_2 = Player(input(), turn='')
    print('Great to meet you, ' + player_2.name + '!')

    print('Now let\'s get started, shall we?')

    print('To begin this wretched game of tic tac toe, you will throw some elbo--I mean dice.')
    throw_dice(player_1, player_2)
    pick_turn(player_1, player_2)

    # The logic of the game itself:
    print('We\'re ready to rumble!! ')
    tic_tac_toe()














    # you gotta take turns doing this thing
    # player one takes a turn, and then player two
    # after someone puts down


# we need to define a player taking a turn on the board, takes player and board move


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tic_tac_toe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
