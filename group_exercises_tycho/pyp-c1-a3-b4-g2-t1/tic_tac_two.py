
"""
To do list

1. setup game
2. ask fir input on each turn
3. check if win condition is met
4. goodbye message and quit

Game initializes with:
init_game

"""

# moves_list is a 1-dimensional list of moves. '' = empty, X = X, O = O
def show_grid(moves_list = ['' for x in range(9)], coords = False):

    # If coords == True, this coordinates grid visualized
    if coords == True:
        print_grid = ([
                'A 1', 'A 2', 'A 3',
                'B 1', 'B 2', 'B 3',
                'C 1', 'C 2', 'C 3'
                ])
                
    # Else: visualized current moves made
    else:
        print_grid = moves_list
    
    
    # The grid visualizer
    width = 5
    for x in range(3):
        for y in range(3):
            print (print_grid[x*3 + y].center(width, ' '), end = ''), 
            if y != 2:
                    print (" | ", end = ''), 
            
        if x != 2:
            print ("\n" + "_" * (width * 3 + 2))
        else:
            print ('\n')
            return moves_list

            
#The game initializer
def init_game():
    print ("""
        Welcome, players! Or player. If you're alone, go find a buddy.
        The first player may begin once you're ready! 
        Type the coordinate (e.g. A1) to mark your spot.
        Anytime you want to see the coordinates, type "grid".
        Good luck! May the best one win!
        """)

    # Show grid for the first time
    show_grid(coords = True)
    
    # Requires any input before we go
    commence = input("""\nOnce you're ready, type "HELL YEAH!" """)
    return make_move('X')



def make_move(act_player, moves_list = ['' for x in range(9)]):
    
    # Input = the move
    print ("""Type "grid" to see grid coordinates.""")
    new_move = input("Choose your move, player {} \n".format(act_player))
    new_move = new_move.upper().replace(' ', '')
    
    # shows grid if asked for
    if new_move == 'GRID':
        show_grid(moves_list, coords = True)
        return make_move(act_player, moves_list)
    
        
    #check for row
    if 'A' in new_move:
        position = 0
    elif 'B' in new_move:
        position = 3
    elif 'C' in new_move:
        position = 6
    else:
        print ("\nHmm.. your input doesn't make sense to me. ", end = '')
        return make_move(act_player)
        
    #add column
    position += int(new_move[1]) - 1
    
    #add move to moves_list
    if moves_list[position] == '':
        moves_list[position] = act_player
    else:
        print ("That position is already taken! ", end = '')
        return make_move(act_player)
    
    
    print ("\n")
    show_grid(moves_list)
    
    if victory_check(act_player, moves_list) == act_player:
        return ("We've got a winner! Player {} takes the prize. Goodbye!".format(act_player))
    elif victory_check(act_player, moves_list) == -1:
        return (input("No one wins. So EVERYBODY wins! Thank you for playing."))
    else:
        # Change active player, go to next turn
        if act_player == 'X':
            act_player = 'O'
        elif act_player == 'O':
            act_player = 'X'
        return make_move(act_player, moves_list)



def victory_check(act_player, moves_list):
    full_board = True #True until proven otherwise
    win = 0
    while True:
        for x in range(3):
            iterlist = [moves_list[y] for y in range(x, x + 7, 3)]
            if iterlist.count(act_player) == 3:
                win = 1
                break
            if '' in iterlist:
                full_board = False
        for x in range(0, 7, 3):
            iterlist = [moves_list[y] for y in range(x, x + 3, 1)]
            if iterlist.count(act_player) == 3:
                win = 1
                break
        diagonal_1 = [moves_list[x] for x in [0,4,8]].count(act_player)
        diagonal_2 = [moves_list[x] for x in [2,4,6]].count(act_player)
        if diagonal_1 == 3 or diagonal_2 == 3:
            win = 1
        break
            
    if win == 1:
        return (act_player)
    elif full_board == True:
        return (-1)
    else:
        return (False)

print (init_game())