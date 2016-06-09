import random
from datetime import datetime


#globals
#ships
comp_sub = []
comp_aircraft = []
comp_patrol1 = []
comp_patrol2 = []
player_sub = []
player_aircraft = []
player_patrol1 = []
player_patrol2 = []
all_ships = []
comp_ships = []
comp_ship_coord = []
player_ships = []
player_ship_coord = []


def initializer():
    '''requests desired starting player,
    fetches board_state
    returns turn(act_player, board_state)'''
    who_starts = input("Do you want to be the starting player? I can choose a starting player at random. (y/n/r)")

    
    if who_starts.lower() == 'y':
        act_player = "human"
    elif who_starts.lower() == 'n':
        act_player = "computer"
    elif who_starts.lower() == 'r':
        if datetime.now % 2 == 0:
            act_player = "human"
        else:
            act_player = "computer"
    else:
        print ("Enter one of the three letters please.")
        return initializer()
    board_state = create_board(player_ships)
    return turn(act_player, board_state)


def check_range(str_input):
    try:
        int_input = int(str_input)
        if int_input not in range(1,11):
            return False
        else: 
            return int_input
    except (Exception, e):
        return False


def create_sub(player):
    global comp_ship_coord, player_ship_coord
    slant_x = random.choice([0,1])
    if slant_x == 0: slant_y = 1
    else: slant_y = 0
    
    if player == "computer":
        cell_1 = [random.randrange(1,11),random.randrange(1,11)]
        ship_coord_list = comp_ship_coord
    else:
        x_coord = input("Input X coordinate for our Submarine")
        x_coord = check_range(x_coord)
        y_coord = input("Input Y coordinate for our Submarine")
        y_coord = check_range(y_coord)
        if x_coord == False or y_coord == False:
            print ("We can only position our ships within range 1 and 10, Sir.")
            return create_sub(player)
        cell_1 = [x_coord - 1, y_coord - 1]
        ship_coord_list = player_ship_coord
    cell_2 = [0,0]
    cell_3 = [0,0]
    #x coordinates
    if cell_1[0] > 8:
        cell_2[0] = cell_1[0] - slant_x
        cell_3[0] = cell_2[0] - slant_x
    else:
        cell_2[0] = cell_1[0] + slant_x
        cell_3[0] = cell_2[0] + slant_x       

    if cell_1[1] > 8:
        cell_2[1] = cell_1[1] - slant_y
        cell_3[1] = cell_2[1] - slant_y
    else:
        cell_2[1] = cell_1[1] + slant_y
        cell_3[1] = cell_2[1] + slant_y      
    
    new_ship = [cell_1,cell_2,cell_3]

    for ship_cell in new_ship:
        for existing_ships in ship_coord_list:
            if ship_cell not in existing_ships:
                continue
            else:
                print ("Careful! One of our ships is already on those coordinates!")
                return create_sub(player)
    ship_coord_list.append(new_ship)
    return new_ship


def create_aircraft(player):
    global comp_ship_coord, player_ship_coord
    slant_x = random.choice([0,1])
    if slant_x == 0: slant_y = 1
    else: slant_y = 0
    
    if player == "computer":
        cell_1 = [random.randrange(1,11),random.randrange(1,11)]
        ship_coord_list = comp_ship_coord
    else:
        x_coord = input("Input X coordinate for our Aircraft Carrier")
        x_coord = check_range(x_coord)
        y_coord = input("Input Y coordinate for our Aircraft Carrier")
        y_coord = check_range(y_coord)
        if x_coord == False or y_coord == False:
            print ("We can only position our ships within range 1 and 10, Sir.")
            return create_aircraft(player)
        cell_1 = [x_coord - 1, y_coord - 1]
        ship_coord_list = player_ship_coord
    cell_2 = [0,0]
    cell_3 = [0,0]
    cell_4 = [0,0]
    cell_5 = [0,0]
    if cell_1[0] > 5:
        cell_2[0] = cell_1[0] - slant_x
        cell_3[0] = cell_2[0] - slant_x
        cell_4[0] = cell_3[0] - slant_x
        cell_5[0] = cell_4[0] - slant_x
        
    else:
        cell_2[0] = cell_1[0] + slant_x
        cell_3[0] = cell_2[0] + slant_x
        cell_4[0] = cell_3[0] + slant_x
        cell_5[0] = cell_4[0] + slant_x

    if cell_1[1] > 5:
        cell_2[1] = cell_1[1] - slant_y
        cell_3[1] = cell_2[1] - slant_y
        cell_4[1] = cell_3[1] - slant_y
        cell_5[1] = cell_4[1] - slant_y
        
    else:
        cell_2[1] = cell_1[1] + slant_y
        cell_3[1] = cell_2[1] + slant_y
        cell_4[1] = cell_3[1] + slant_y
        cell_5[1] = cell_4[1] + slant_y
        
    new_ship = [cell_1,cell_2,cell_3,cell_4,cell_5]

    for ship_cell in new_ship:
        for existing_ships in ship_coord_list:
            if ship_cell not in existing_ships:
                continue
            else:
                print ("Careful! One of our ships is already on those coordinates!")
                return create_aircraft(player)
    ship_coord_list.append(new_ship)
    return new_ship


def create_patrol(player):
    global comp_ship_coord, player_ship_coord
    slant_x = random.choice([0,1])
    if slant_x == 0: slant_y = 1
    else: slant_y = 0
    
    if player == "computer":
        cell_1 = [random.randrange(1,11),random.randrange(1,11)]
        ship_coord_list = comp_ship_coord
    else:
        x_coord = input("Input X coordinate for our Patrol Ship")
        x_coord = check_range(x_coord)
        y_coord = input("Input Y coordinate for our Patrol Ship")
        y_coord = check_range(y_coord)
        if x_coord == False or y_coord == False:
            print ("We can only position our ships within range 1 and 10, Sir.")
            return create_patrol(player)
        cell_1 = [x_coord - 1, y_coord - 1]
        ship_coord_list = player_ship_coord
    cell_2 = [0,0]
    if cell_1[0] > 8: cell_2[0] = cell_1[0] - slant_x
    else: cell_2[0] = cell_1[0] + slant_x
    
    if cell_1[1] > 8: cell_2[1] = cell_1[1] - slant_y
    else: cell_2[1] = cell_1[1] + slant_y
        
    new_ship = [cell_1,cell_2]

    for ship_cell in new_ship:
        for existing_ships in ship_coord_list:
            if ship_cell not in existing_ships:
                continue
            else:
                print ("Careful! One of our ships is already on those coordinates!")
                return create_patrol(player)
    ship_coord_list.append(new_ship)
    return new_ship


def create_ships(board_state = None):
    '''
    Container for ship creation functions.
    Triggered at beginning of game.
    '''
    global comp_sub, comp_aircraft, comp_patrol1, comp_patrol2, player_sub, player_aircraft, player_patrol1, player_patrol2, all_ships, comp_ships, player_ships
    comp_sub = create_sub("computer")
    comp_aircraft = create_aircraft("computer")
    comp_patrol1 = create_patrol("computer")
    comp_patrol2 = create_patrol("computer")
    comp_ships = [comp_sub, comp_aircraft, comp_patrol1, comp_patrol2]
    
    player_ships_creator = [create_sub, create_aircraft, create_patrol, create_patrol]
    player_ships = []
    
    for ship in player_ships_creator:
        player_ships.append(ship("player"))
        board_state = create_board(player_ships, board_state)
        board_state = show_board(board_state, only_playerboard = 1)
    all_ships = [comp_ships, player_ships]
    

def create_board(player_ships, board_state = None):
    if board_state == None:
        board_state = [[[[' ' for cell_posit in range(3)] for cell in range(10)] for row in range(10)] for board in range(2)]   #creates two boards for both players
    ship_letter_dict = {3: "S", 5: 'A', 2: "P"}
    for ship in player_ships:
        for ship_coord in ship:
            board_state[1][ship_coord[0]][ship_coord[1]][1] = ship_letter_dict[len(ship)]
    return board_state
    
def new_board():
    board = []
    for i in range(1,11):
        for j in range(1,11):
            board.append([i,j])
    return board
            
    
def show_board(board_state, only_playerboard = 0):
    '''
    within the board, len(cell) = 3, e.g. "X X"
    cell[0] = cell[2] = empty if not shot, "X" if shot
    cell[1] = "S" if submarine, "A" if aircraft, "P" if patrol boat
    '''
    if board_state == None:
        board_state = [[[[' ' for cell_posit in range(3)] for cell in range(10)] for row in range(10)] for board in range(2)]   #creates two boards for both players
    board_tag = "The opponent's board state:"

    for board in board_state:
        if only_playerboard == 1:
            only_playerboard = 0
            board_tag = "Your board state:"
            continue
        print (board_tag)
        print ("_"*6*10)
        
        for row in board:
            print ("|", end=" ")
            for cell in row:
                print ("".join(cell), "| ", end="")
            print ("\n" + "_"*6*10)
        board_tag = "Your board state:"
    return board_state
        
  
def shoot_request(message):
    shot = check_range(input(message))
    if shot == False:
        print ("We can't shoot there!", end=" ")
        return shoot_request(message)
    else:
        return shot


def yn_confirmation(message):
    answer = input(message)
    if answer.lower() not in ('y','n'):
        print ("We need a clear answer!", end=" ")
        return yn_confirmation(message)
    else:
        return answer


def shooting(act_player, board_state):
    '''
    Asks for coordinates, marks the coordinates
    checks hit_ship() if hit, adjusts the board_state accordingly
    Else returns board_state
    '''
    if act_player == "computer":
        shoot_board = 1
        hit_message = "Our enemy hit our {}!"
        shoot_x, shoot_y = random.randrange(1,11), random.randrange(1,11)

        
    elif act_player == "human":
        shoot_board = 0
        hit_message = "We hit a ship! It seems to be a {}! Good job sir!"
        shoot_x = shoot_request("Give us an order where to shoot! What's the X coordinate?")
        shoot_y = shoot_request("What's the Y coordinate?")
    
    if board_state[shoot_board][shoot_x][shoot_y][0] == ' ':
        if act_player == "human":
            confirmation = yn_confirmation("You gave us the coordinates {x}, {y}. Ready!? (y/n)".format(x = shoot_x, y = shoot_y))
            if confirmation == 'y':
                shoot_x -= 1
                shoot_y -= 1
            elif confirmation == 'n':
                print ("Awaiting new orders!")
                return shooting(act_player, board_state)
    else:
        if act_player == human:
            print ("We've already shot there, let's try other areas!")
        return shooting(act_player, board_state)
      
    #below happens for both      
    board_state[shoot_board][shoot_x][shoot_y][0], board_state[shoot_board][shoot_x][shoot_y][2] = "x", "x"
    hit_ship_check = hit_ship(shoot_x, shoot_y, board_state, act_player)
    if hit_ship_check == False:
        return board_state
    else:
        board_state[shoot_board][shoot_x][shoot_y][1] = hit_ship_check[0]
        print (hit_message.format(hit_ship_check[1]))
    pause = input("Give us the sign and we'll show you the battlefield!")
    return board_state
 
 
def enemy_ship_list(active_player):
    '''
    Returns the ship list for the opposing player
    '''
    if active_player == "computer":
        searchlist = comp_ships
    elif active_player == "human":
        searchlist = player_ships
    return searchlist


def find_ship_identity(ship):
    a = len(ship)
    if a == 2: return ["P", "Patrol"]
    elif a == 3: return ["S", "Submarine"]
    elif a == 5: return ["A", "Aircraft Carrier"]
   
    
def hit_ship(guess_x, guess_y, board_state, active_player):
    searchlist = enemy_ship_list(active_player)
    for ship in searchlist:
        if [guess_x, guess_y] in ship:
            ship_id = find_ship_identity(ship)
            return ship_id
        else:
            return False
 
            
def turn(act_player, board_state):
    '''
    A general turn, loops until win_check == True
    args:
    act_player (human = manual turn, comp = automatic turn)
    board_state (necessary for win_check and show_board)
    '''
    if act_player == "human":
        show_board(board_state)
    shooting(act_player, board_state)
    
    if win_check(act_player, board_state) == True:
        return end_game(act_player, board_state)
    else:
        show_board(board_state)
        if act_player == "computer":
            act_player = "human"
        elif act_player == "human":
            act_player = "computer"
        return turn(act_player, board_state)

    
def win_check(act_player, board_state):
    '''
    checks if either board still contains unshot ship-cells
    '''
    for board in board_state:
        for row in board:
            for cell in row:
                if ''.join(cell[0][:2]) != "x ":
                    return False
                else:
                    return True


def end_game(act_player, board_state):
    if act_player == "computer":
        print ("The computer has bested you! Well, by all means, return when you have built your new fleet.")
    elif act_player == "human":
        print ("You have won! Congratulations, you did well!")
    
    #print which ships were left
    
    print ("Thank you for playing!")
    print ("Credits:")
    print ("A lot of stuff - Avi Schwartz")
    print ("Also quite some stuff - Tycho van Kleef")


def new_game():
    '''
    New game state
    '''
    global comp_sub, comp_aircraft, comp_patrol1, comp_patrol2, player_sub, player_aircraft, player_patrol1, player_patrol2, all_ships
    
    #reinitializes global variables
    comp_sub = []
    comp_aircraft = []
    comp_patrol1 = []
    comp_patrol2 = []
    player_sub = []
    player_aircraft = []
    player_patrol1 = []
    player_patrol2 = []
    player_ships = []
    comp_ships = []
    all_ships = []
    comp_ship_coord = []
    player_ship_coord = []
    
    #calling games functions
    board_state = show_board(None, only_playerboard = 1)    #prints own board and stores board_state variable
    create_ships(board_state)   #randomly generates all ships
    
                    #lets player choose coordinates for his/her ships
    initializer()   #collects user input, for who goes first, fetches board_state from create_board, gives act_player and board_state to turn()
    turn(act_player, board_state) 


#calling funct - needs to be at bottom
new_game()