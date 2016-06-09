__author__ = 'Avi Schwartz, Schwartz210@gmail.com'
from tkinter import *

master = Tk()
master.title("Tic Tac Toe")
WIDTH = 300
HEIGHT = 300
box_width = WIDTH / 3
box_height = HEIGHT / 3
half_box_width = box_width / 2
half_box_height = box_height / 2
boxes_in_play = set([])

canvas = Canvas(master, width=WIDTH, height=HEIGHT)

def switch_player():
    global active_player, inactive_player
    if active_player == player1:
        active_player = player2
        inactive_player = player1
    elif active_player == player2:
        active_player = player1
        inactive_player = player2
    else: print("error")

class Player:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.boxes = []

    def add_box(self, new_box):
        if new_box not in self.boxes and new_box not in inactive_player.boxes:
            self.boxes.append(new_box)
            boxes_in_play
            canvas.create_text(box_width * new_box[0] - half_box_width, box_height * new_box[1] - half_box_height, text=self.text)

    def victory_condition(self):
        '''
        Evualuates if victory condition is met
        '''
        v1 = [[1,1], [1,2], [1,3]]
        v2 = [[2,1], [2,2], [2,3]]
        v3 = [[3,1], [3,2], [3,3]]
        v4 = [[1,1], [2,1], [3,1]]
        v5 = [[1,2], [2,2], [3,2]]
        v6 = [[1,3], [2,3], [3,3]]
        v7 = [[1,1], [2,2], [3,3]]
        v8 = [[1,3], [2,2], [3,1]]
        victory_conditions = [v1,v2,v3,v4,v5,v6,v7,v8]
        for victory_condition in victory_conditions:
            points = 0
            for item in victory_condition:
                if item in self.boxes:
                    points += 1

            if points == 3:
                print(self.name + " Victory")


player1 = Player("Player1","XXXXX")
player2 = Player("Player2","O")

active_player = player1 #player1/player2 switch off being active/inactive
inactive_player = player2

def refresh_grid():
    '''
    Creates the grid on the canvas.
    '''
    grid_size = 3
    for i in range(grid_size):
        for j in range(grid_size):
            canvas.create_rectangle(i * box_width ,j * box_height, i * box_width + box_width, j * box_height + box_height, fill="Red")

def callback(event):
    '''
    This is the mouseclick handler. This block of code executes everytime the mouse is clicked.
    '''
    global player, text
    coord = [event.x, event.y]
    box = [0,0]

    #Takes x coordinates from mouseclick and convert them to cells
    if coord[0] < box_width * 1: box[0] = 1
    elif coord[0] < box_width * 2: box[0] = 2
    elif coord[0] < box_width * 3: box[0] = 3
    else: box[0] = "error"

    #Takes y coordinates from mouseclick and convert them to cells
    if coord[1] < box_height * 1: box[1] = 1
    elif coord[1] < box_height * 2: box[1] = 2
    elif coord[1] < box_height * 3: box[1] = 3
    else: box[1] = "error"

    active_player.add_box(box)
    active_player.victory_condition()  #evaluates if victory condition is met
    switch_player()


refresh_grid()
canvas.bind("<Button-1>", callback)
canvas.pack()
master.mainloop()
