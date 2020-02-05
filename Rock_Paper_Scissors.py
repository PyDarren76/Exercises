import random

def display_game_rules():
    print('''\n\n\t\t\tROCK, PAPER, SCISSORS GAME RULES
            ---------------------------------------------------------
               Pick #1 for "Rock"
               Pick #2 for "Paper"
               Pick #3 for "Scissors"
               * If one picks "Rock" and the other picks "Scissors", --> "Rock" Wins
               * If one picks "Scissors" and the other picks "Paper", --> "Scissors" Wins
               * If one picks "Paper" and the other picks "Rock", --> "Paper" Wins
               * If both player make the same choice, --> It's a Tie 
               * Game ends when either player gets to 5 wins...
               GOOD LUCK ! \n
            ''')

def generate_rnd_number():
    '''Returns a random number for the computer pick...'''
    rnd_number = random.randint(1, 3)
    return rnd_number

display_game_rules()

def get_user_pick():
    '''Returns the player's selection...'''
    plyr_pick = 0
    while plyr_pick < 1 or plyr_pick > 3:
        try:
            plyr_pick = int(input('Enter your choice  1.for rock, 2.for paper, or 3.for scissors  -->>   '))
        except ValueError:
            print('ERROR! Please enter a valid selection...')
    return plyr_pick
#-------------------------------------------------------------
pc_cnt = 0
ply_cnt = 0

def decide_winner(pc, plyr):
    global pc_cnt
    global ply_cnt
    if ((pc == 1) and (plyr == 1)):
        print('Computer: Rock  -----  Player: Rock  -->>  It is a Tie !')
    elif ((pc == 1) and (plyr == 2)):
        print('Computer: Rock  -----  Player: Paper  -->>  Player Wins !')
        ply_cnt = ply_cnt + 1
    elif ((pc == 1) and (plyr == 3)):
        print('Computer: Rock  -----  Player: Scissors  -->>  Computer Wins !')
        pc_cnt = pc_cnt + 1
    elif ((pc == 2) and (plyr == 1)):
        print('Computer: Paper  -----  Player: Rock  -->>  Computer Wins !')
        pc_cnt = pc_cnt + 1
    elif ((pc == 2) and (plyr == 2)):
        print('Computer: Paper  -----  Player: Paper  -->>  It is a Tie !')
    elif ((pc == 2) and (plyr == 3)):
        print('Computer: Paper  -----  Player: Scissors  -->>  Player Wins !')
        ply_cnt = ply_cnt + 1
    elif ((pc == 3) and (plyr == 1)):
        print('Computer: Scissors  -----  Player: Rock  -->>  Player Wins !')
        ply_cnt = ply_cnt + 1
    elif ((pc == 3) and (plyr == 2)):
        print('Computer: Scissors  -----  Player: Paper  -->>  Computer Wins !')
        pc_cnt = pc_cnt + 1
    elif ((pc == 3) and (plyr == 3)):
        print('Computer: Scissors  -----  Player: Scissors  -->>  It is a Tie !')

#----------------------------------------------------------------------
game_count = 0

while pc_cnt <= 4 and ply_cnt <= 4:
    computer = generate_rnd_number()  # Holds the random number for the computer..
    player = get_user_pick()  # Holds the player's pick...
    decide_winner(computer, player)
    print('Total Computer Wins:', pc_cnt, '& Total Player Wins:', ply_cnt)
    print('-' * 40)
    game_count += 1







