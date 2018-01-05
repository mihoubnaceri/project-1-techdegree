import random
import sys
import os

# draw the grid
# pick random place for player
# pick random place for exit door
# pick random place for monster
#draw player
# take input for movement
# move player in a vallid way

#check for win/loss
# clear screen and redraw grid
CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),
         (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),
         (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),
         (0,3),(1,3),(2,3),(3,3),(4,3),(5,3),
         (0,4),(1,4),(2,4),(3,4),(4,4),(5,4),
         (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)]

def clear():
    os.system("cls" if os.name=="nt" else "clear")
def get_locations():
    return random.sample(CELLS,3)

def move_player(player,moves):
    # left moves x-1
    x,y = player
    if moves == "LEFT":
        x-=1
    elif moves == "RIGHT":
        x+=1
    elif moves == "UP":
        y-=1
    elif moves == "DOWN":
        y+=1

    #right moves x+1
    #up moves y-1
    #down moves y+1
    return (x,y)
def get_moves(player):
    moves = ["LEFT","RIGHT","UP","DOWN"]
    x,y = player
    if x ==0:
        moves.remove("LEFT")
    if x == 5:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 5:
        moves.remove("DOWN")
    return moves

def draw_map(player):
    print(" _"*6)
    tile = "| {}"
    for cell in CELLS:
        x,y = cell
        if x < 5:
            line_end=""
            if cell==player:
                output= tile.format("X")
            else:
                output= tile.format("_")
        else:
            line_end = "\n"
            if cell== player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output,end=line_end)

def game_loop():
    player,monster,door = get_locations()
    while True:
        clear()
        draw_map(player)
        valid_moves = get_moves(player)

        print("You are at door number {}".format(player)) # position of player
        print("try to find the secret door")
        print("you can move {}".format(", ".join(valid_moves))) # print available moves depending on the get_moves func
        print("type 'QUIT' TO quit")
        print("doors pos {}".format(door))
        print("monsters at {}".format(monster))
        move = input("> ").upper()
        if move == "QUIT":
            print("Thanks for playing!")
            break
        # if good move? than make move
        if move in valid_moves:
            player = move_player(player,move)
        #if invalid move dont move
        elif move not in ["LEFT","RIGHT","UP","DOWN"]:
            print("not valid command")
        else:
            input("you just hit a wall hahhaha fucking funny")
            clear()
        #if on doors position than they win mate ;)
        if door == player:
            print("yOU FOUND Thte door congrats youa re free!")
            break
        # on monsters position you lose
        if monster == player:
            print("you fucking lose bitch")
            break
        # else loop around
        else:
            continue
        clear()
clear()
print("Wlecome to the game")
input("press enter to start")
clear()
game_loop()
