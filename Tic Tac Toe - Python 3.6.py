############ Definitions #####################

#This is the dictionary to be converted to the printed board.
dic = {'A':'A','B':'B','C':'C','D':'D','E':'E','F':'F','G':'G','H':'H','I':'I'}

#These letters represent the blocks on the board,
# the player can only choose among these,
# and once a player makes a move the applicable letter is removed from this list.
leftmoves = ['A','B','C','D','E','F','G','H','I']


#This counts the moves\rounds - if it gets to 10 and there
# is no winner - the checkwinner function will call the game a tie.
r = 1

#This will be replaced by either 'X' or 'O' after each move.
# The upboard() function will use its output to replace the
# applicable letter on the board to be 'X' or 'O' accordingly
currentmove = 0


############ Functions #####################

#This function is used for purposes of delaying the program
# until the user presses Enter.
def anykey():
    input('press Enter to continue')

#This function prints the board.
# the value under attached to each key(row) contains a variable
# which is equal to the value of its key as appears in "dic",
# those values in "dic" will change to X or O as the game rolls.
def pboard():
    ''' This function prints the current board '''
    board = {'row1':'    *    *','row2':'  '+dic.get('A')+' * '+dic.get('B')+'  * '+dic.get('C'),'row3':'*************','row4':'  '+dic.get('D')+' * '+dic.get('E')+'  * '+dic.get('F'),'row5':'*************','row6':'  '+dic.get('G')+' * '+dic.get('H')+'  * '+dic.get('I'),'row7':'    *    *'}
    print('\n\n')
    for i,row in enumerate(board):
        print(list(board.values())[i])

#This function updates the board after the player makes a move by
#converting his input to either X or O and placing it on the board
# by dictionary value of the applicable letter to either 'X' or 'O'
def upboard():
    '''This function updates the board by move number'''
    global currentmove
    global r
    if r % 2 == 0:
        n = 'O'
        r+=1
    else:
        n = 'X'
        r+=1
    dic.update({currentmove:n})
    return pboard()

#This function used to check if there is a winner, a tie,
#or just to inform the palyers that there is no winner yet.
# The use of this function commences after move 5,
# as prior to move #5 there are not enough moves to call a winner.
def checkwinner():
    check = 0
    if dic.get('A') == dic.get('B') == dic.get('C') or  dic.get('D') == dic.get('E') == dic.get('F') or dic.get('G') == dic.get('H') == dic.get('I') or dic.get('A') == dic.get('D') == dic.get('G') or dic.get('B') == dic.get('H') == dic.get('I') or dic.get('C') == dic.get('F') == dic.get('I') or dic.get('A') == dic.get('E') == dic.get('I') or dic.get('C') == dic.get('E') ==dic.get('G'):
        check = 1
        if dic.get('A') == dic.get('B') == dic.get('C'):
            if dic.get('A') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('D') == dic.get('E') == dic.get('F'):
            if dic.get('D') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('G') == dic.get('H') == dic.get('I'):
            if dic.get('G') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('A') == dic.get('D') == dic.get('G'):
            if dic.get('A') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('B') == dic.get('H') == dic.get('I'):
            if dic.get('B') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('C') == dic.get('F') == dic.get('I'):
            if dic.get('C') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('A') == dic.get('E') == dic.get('I'):
            if dic.get('A') == 'X':
                w = playerx1
            else:
                w = playerx2
        elif dic.get('C') == dic.get('E') == dic.get('G'):
            if dic.get('C') == 'X':
                w = playerx1
            else:
                w = playerx2
        print('%s YOU ARE THE WINNER!!!!!!!!!!' % w)
        input('Press ENTER to exit')
    if check == 0 and r != 10:
        print('No winner yet, lets continue!\n')
    if r == 10:
        print('Game Over - This is a Tie!')
        input('Press ENTER to exit')

#This function is used to make to get the input of the applicable
# move from the relevant player and to make sure that the input is
# among the possible options.
def currentmovef():
    global currentmove
    global leftmoves
    check = 0
    while check == 0:
        currentmove = input('Please enter your choice').upper()
        if currentmove not in leftmoves:
            print('Please insert one of the following moves: %s' %leftmoves)
        else:
            check+=1
            leftmoves.pop(leftmoves.index(currentmove))


############ Game Starts #####################

#Opening with greeting
print('Lets start playing!')
anykey()

print('here is the Board!')
pboard()

#This is to get the name of the players and to make sure that the
# characters are a-z, not longer than 10 letters and that the names
# are not the same (capital sensitive).
print('Player 1, please enter your name and press Enter')
name1 = 0
while name1 == 0:
    import re
    import string
    global player1
    player1 = input("Enter name:")
    for l in player1:
        if l not in list(string.ascii_letters):
            print('Please use only alphabetic letters')
            break
        elif len(player1) > 10:
            print('Please make sure the name you entered is shorter than 10 characters')
            break
        else:
            name1+=1

print('Player 2, please enter your name and press Enter')
name2 = 0
while name2 == 0:
    import re
    import string
    global player2
    player2 = input("Enter name:")
    if player2 == player1:
        print('Cant have the same name!')
    else:
        for l in player2:
            if l not in list(string.ascii_letters):
                print('Please use only alphabetic letters')
            elif len(player2) > 10:
                print('Please make sure the name is shorter than 10 characters')
            else:
                name2+=1

print('\nWelcome '' '+player1+' and '+player2+'!\n')

import random #this is to randomly choose who starts
playerx1 = random.choice([player1,player2])

#then the following code automatically assigns the other to be the second
playerx2 = [x for x in [player1,player2] if playerx1 != x][0]

print('%s, \n Congrats! \n You have been randomly chosen to make the first move! \n You are assigned to be "X"\n' %playerx1)
print('%s,\n you are second to go, \n and assigned to be "O"\n' %playerx2)
anykey()

#1 Move
print('%s, Please make the first move,\n by inserting the letter in the block where you wish to place your X' %playerx1)
pboard()
#The input has to be one of the letters left somehow
currentmovef()
upboard()

#2 Move
print('Nice Move! '+playerx2+', now it is your turn to make a move:')
currentmovef()
upboard()

#3 Move
print('Nice Move! '+playerx1+', now it is your turn to make a move:')
currentmovef()
upboard()

#4 Move
print('Nice Move! '+playerx2+' now it is your turn to make a move:')
currentmovef()
upboard()

#5 Move
print('Nice Move! '+playerx1+', now it is your turn to make a move:')
currentmovef()
upboard()

#6 Move
checkwinner()
print(playerx2+', now it is your turn to make a move:')
currentmovef()
upboard()

#7 Move
checkwinner()
print(playerx1+' now it is your turn to make a move:')
currentmovef()
upboard()

#8 Move
checkwinner()
print(playerx2+', now it is your turn to make a move:')
currentmovef()
upboard()

#9 Move
checkwinner()
print(playerx1+', now it is your turn to make a move:')
currentmovef()
upboard()
checkwinner()
