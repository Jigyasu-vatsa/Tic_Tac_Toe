#Dict for TicTacToe

board = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' ' }

#Dict for TicToeToe Move Records
recordDict = {'T1': '00', 'T2': '01', 'T3': '02','M1': '10', 'M2': '11', 'M3': '12','D1': '20', 'D2': '21', 'D3': '22' }


player = 1  # to initialise first player
total_moves = 0     # to count the moves end_check = 0 

#all check cons declared here


def check():    # checking the moves of player one     
# for horizontal(start)     
    if board['T1'] == player1symbol and board['T2'] == player1symbol and board['T3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    if board['M1'] == player1symbol and board['M2'] == player1symbol and board['M3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    if board['D1'] == player1symbol and board['D2'] == player1symbol and board['D3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    # for horizontal(end)
    # for diagonal(start)
    if board['T1'] == player1symbol and board['M2'] == player1symbol and board['D3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    # for diagonal(end)
    # for vertical(start)
    if board['T1'] == player1symbol and board['M1'] == player1symbol and board['D1'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    if board['T2'] == player1symbol and board['M2'] == player1symbol and board['D2'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    if board['T3'] == player1symbol and board['M3'] == player1symbol and board['D3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    if board['D1'] == player1symbol and board['M2'] == player1symbol and board['T3'] == player1symbol:
        print('{} won !'.format(player1))
        fl.write('{} won !'.format(player1))
        return 1
    # for vertical(end)
    # checking the moves of player two
    if board['T1'] == player2symbol and board['T2'] == player2symbol and board['T3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
        # used to end the game
    if board['M1'] == player2symbol and board['M2'] == player2symbol and board['M3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['D1'] == player2symbol and board['D2'] == player2symbol and board['D3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['T1'] == player2symbol and board['M2'] == player2symbol and board['D3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['T1'] == player2symbol and board['M1'] == player2symbol and board['D1'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['T2'] == player2symbol and board['M2'] == player2symbol and board['D2'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['T3'] == player2symbol and board['M3'] == player2symbol and board['D3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        return 1
    if board['D1'] == player2symbol and board['M2'] == player2symbol and board['T3'] == player2symbol:
        print('{} won !'.format(player2))
        fl.write('{} won !'.format(player2))
        
        return 1
    return 0

player1 = input("\n\t \t Tic-Tac-Toe\n\nEnter Player1 Name: ").capitalize()

#when user not entered name for player1
if len(player1)==0:
    player1="Jig's"
    print("\nDefault name for player1 assigned is: {}".format(player1))
else:
    pass

player2 = input("Enter Player2 Name: ").capitalize()

#when user not entered name for player2
if ((len(player2)==0) | (player1==player2)):
    player2="Anonyms"
    print("\nDefault name for player2 assigned is: {}\n".format(player2))
else:
    pass

#Welcome Greeting to Players

#Symbol initalization

player1symbol = input("\nWelcome,\n{} & {}....\nEnter symbol for {}: ".format(player1,player2,player1)).upper()

#when user not entered any symbol for player1
while len(player1symbol)!=1:
        
    if len(player1symbol)==0:
        player1symbol="X"
        print("\nDefault symbol for {}: {}\n".format(player1.upper(),player1symbol))
    else:
        player1symbol = input("\nWrong symbol choice!\nEnter single character symbol for {}: ".format(player1)).upper()
    
player2symbol = input("Enter symbol for {} other than {}: ".format(player1,player1symbol)).upper()


#when user not entered any symbol for player 2 or wrong symbol
while ((len(player2symbol)!=1) | (player2symbol == player1symbol)) :
        
    if len(player2symbol)==0:
        player2symbol="0"
        print("\nDefault symbol for {}: {}\n".format(player2.upper(),player2symbol))
    elif player2symbol==player1symbol:
        player2symbol = input("\nAlready Used!\nEnter another symbol for {}: ".format(player2)).upper()
    else:
        player2symbol = input("\nWrong symbol choice!\nEnter single character symbol for {}: ".format(player2)).upper()

    
print("\nWelcome", player1, "and",player2, "\nNow,\n\tYou both have successfully entered into our \"Tic-Tac-Toe\" game play zone")
input("Get ready,\nPress any key to start the game....")

#First time display of game grid

print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3\n')

#record all moves into a fle in csv/txt file format
#import csv

fl = open("TicTacToeRecordFile.txt",'a')
#wrtfl=csv.writer(fl)
fl.write("\n")
fl.write("player1: {}\n".format(player1))
fl.write("player2: {}\n".format(player2))
fl.write("")

#User gameplay starts from here

while True:
    end_check = check()
    if ((total_moves == 9) & (end_check !=1)):
        print('\t*Match Draw!*\t')
        fl.write("\t*Match Draw!*\t")
        fl.write("\n*End*\n")
        fl.write("")
        fl.close()
        break
    elif end_check == 1:
        fl.write("\n*End*\n")
        fl.write("")
        fl.close()
        break
    while True:     # input from players
        if player == 1:     # choose player
            p1_input = input('{} move: '.format(player1))
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = player1symbol
                fl.write("1 {} {}\n".format(player1symbol,recordDict[p1_input.upper()]))
                player = 2
                break           # on wrong input
            else:
                print('Invalid input, please try again\nYour move: ')
                continue
        else:
            p2_input = input('{} move: '.format(player2))
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = player2symbol
                fl.write("2 {} {}\n".format(player2symbol,recordDict[p2_input.upper()]))
                player = 1
                break
            else:       # on wrong input
                print('Invalid input, please try again\n Your move: ')
                continue
        
    total_moves += 1
    print('***************************')
    print()

    #printing cells to show the live game grid
        
    print('T1|T2|T3' +'\t  \t'+ board['T1']+'|'+board['T2']+'|'+board['T3'])
    print('- +- +- ' +'\t=>\t'+ '-+-+-')
    print('M1|M2|M3' +'\t  \t'+ board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('- +- +- ' +'\t=>\t'+ '-+-+-')
    print('D1|D2|D3' +'\t  \t'+ board['D1'] + '|' + board['D2'] + '|' + board['D3'])
    print()
    
#See Off Greeting Players
    
print("\n\nThank-you for exploring us,", player1, "and",player2,"!")

