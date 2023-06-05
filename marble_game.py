import sys
import random 

class Game_start():
    def __init__(self, red_marbles, blue_marbles):
        self.red_marbles = red_marbles
        self.blue_marbles = blue_marbles
    
    def evaluation_function(self):
        final_state = (self.red_marbles * 3 + self.blue_marbles * 2)
        return final_state
    
    def computers_turn(self):
        colors = ['red', 'blue']
        choose = random.choice(colors) #to randomly select the colors
        if choose == 'red':
            self.red_marbles -= 1
        elif choose == 'blue':
            self.blue_marbles -= 1
            
    def Players_turn(self, player_choose):
        if player_choose == 'red':
            self.red_marbles -= 1
        elif player_choose == 'blue':
            self.blue_marbles -= 1
        else:
            print("You can choose only red or blue marbles.")

if len(sys.argv) < 3:
    print("Usage: python filename.py <red_marble> <blue_marble>")
    sys.exit(1)
# in this context 1 and 2 are the indices of the first and second command-line arguments passed to the Python script. 
red_marbles = int(sys.argv[1])  
blue_marbles = int(sys.argv[2])
game = Game_start(red_marbles, blue_marbles)

# iterating over each of the participants turns
while game.red_marbles > 0 and game.blue_marbles > 0:
    print(f"Red marbles: {game.red_marbles}, Blue marbles: {game.blue_marbles}")
    game.computers_turn()
    if game.red_marbles == 0 or game.blue_marbles == 0:
        break
    player_color = input("Choose a red or blue marble: ").lower()
    game.Players_turn(player_color)

# this print statement keeps track of the red and blue marbles
print(f"Red marbles: {game.red_marbles}, Blue marbles: {game.blue_marbles}")

if game.red_marbles > 0 and game.blue_marbles == 0:
    print(f"Player wins with a score of {game.evaluation_function()}")
elif game.red_marbles == 0 and game.blue_marbles > 0:
    print(f"Computer won with a score of {game.evaluation_function()}")
else:
    print("It's a tie.")
