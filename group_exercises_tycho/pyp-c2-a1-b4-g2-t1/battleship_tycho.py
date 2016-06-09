from datetime import datetime
import copy

class PlayerResources:
    cur_board_state = [[['' for x in range(10)] for y in range(10)] for z in range(2)]
    
    ships = {"submarine" : {"size" : 3, "amount" : 1, "locations" : [None, None, None]},
        "aircraft" : {"size" : 5, "amount" : 1, "locations" : [None, None, None, None, None]}, 
        "patrol_boat" : {"size" : 2, "amount" : 2, "locations" : [[None, None],[None, None]]}}

        
    def __init__(self, player_type):
        self.player_type = player_type
        self.take_shot = ''
        
    def ai_or_not(self):
        if player_type == "computer":
            pass
            #variable = computer, so automation?
        elif player_type == "human":
            #variable = human, so choices
            pass
            
            
    def init_ships(self):
        #first remove all instances?
        PlayerResources.ships_alive = {"computer" : copy.deepcopy(ships), "human" : copy.deepcopy(ships)}
        
            
    def show_grid(cur_board_state):
        board_tag = "The opponent's board state:"
        
        
        for board in PlayerResources.cur_board_state:
            print (board_tag)
            print ("_"*20)
            
            for row in board:
                print ("|", end=" ")
                for cell in row:
                    print (cell, " |", end=" ")
                print ("\n" + "_"*20)
            board_tag = "Your board state:"
    

    def ship_placement(ships):    
        '''
        placement of the ships on the grid
        '''
        for key in ships:
            
        pass
    
    def shot_placement(self):
        '''
        Placement of the opponent's shots
        '''     
        if shot in 
        pass
    
        '''
        Has a player's:
        1. shell grid
        2. shots against the player
        3. ships placed by player
        '''


    


    
'''determine and declare turns (def/at)'''
def turn(player, game_state):
    '''
    Whatever happens in a turn
    '''

    '''
    if act_player = human, show grid
    '''
    
    '''
    if act_palyer = human, ask for a shot
    else place a random shot
    '''
    
    '''
    if act_player = human, show resulting grid
    '''
    pass
    
    

'''placing ships
1. by player
2. by computer
'''

    


def initializer():
    who_starts = input("Who starts: you, the computer, or random? (m/c/r)")
    if who_starts.lower() == 'm':
        return player_state('human')
    elif who_starts.lower() == 'c':
        return player_state('computer')
    elif who_starts.lower() == 'r':
        if datetime.now % 2 == 0:
            return player_state('computer')
        else:
            return player_state('human')
    else:
        print ("Enter one of the three letters.")
        return initializer()
        
def win_con(act_player, player_resources):
    if player_resources.grid == 1:
        pass

        
def game_loop(act_player):
    
    act_player.grid()
    act_player.turn()
    act_player.grid()
    
    if act_player.game_state.win_cond() == 1:
        if act_player == human:
            print (" superhappy message because the test subjet won.")
        else:
            print ("Computers are superior. You know that, right.")
        return "act_player.reset() game state play again or exit..."
    
    if act_player == human:
        return game_loop(computer)
    else:
        return game_loop(human)




###################### ACTION COMMANDS #########################        
#act_player = initializer()
#game_loop(act_player)

            
#human = instance of mainclass
#computer = instance of mainclass  
human = PlayerResources('human')
computer = PlayerResources('computer')    

human.show_grid()

    
        
