import os
os.system("clear")

class Board(): 
    def __init__(self):
        #storing X and O in this list
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        
    def display(self):
        print(" %s | %s | %s" %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s" %(self.cells[7], self.cells[8], self.cells[9]))
        
    #update cells after player input class method    
    def update_cell(self, cell_no, player): 
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
            
    # 8 ways to win class method        
    def winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        
        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        
        return False
            
     
    def reset_board(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #tied game class method
    def tie_game(self):
        used_cells = 0 #assuming board is empty
        for cell in  self.cells: #for each cell in the board (self.cells)
            if  cell != " ": #if a cell is not empty
                used_cells  += 1 #add 1 to the counter
        if used_cells == 9: #if cell counter gets to 9
            return True
        else:
            return False
        
        
#object
board = Board()

def print_header():
    print("Welcome to Tic Tac Toe\n")
    
def refresh_screen():
    #clear the screen
    os.system("clear")
    
    #print header
    print_header()
    
    #display the board
    board.display()
    
    
while True:
    refresh_screen()
    
    #get x input
    x_choice = int(input("\nX) Please choose 1 - 9 > "))
        
    
    #update board
    board.update_cell(x_choice, "X")
    
    
    #refresh screen
    refresh_screen()
    
    #check for X win
    if board.winner("X"):
        print("\nX Wins!\n")
        play_again = input("Play again? (y/n) > ")
        if play_again == "y":
            board.reset_board()
            continue
        else:
            break
        
    #check for tie game
    if board.tie_game():
        print("\nTie Game\n")
        play_again = input("Play again? (y/n) > ")
        if play_again == "y":
            board.reset_board()
            continue
        else:
            break
    
        
    
    #get o input
    o_choice = int(input("\nO) Please choose 1 - 9 > "))
    
    
    #update board
    board.update_cell(o_choice, "O")
    
    #refresh screen
    refresh_screen()
    
    #check for O win
    if board.winner("O"):
        print("\nO Wins!\n")
        play_again = input("Play again? (y/n) > ")
        if play_again == "y":
            board.reset_board()
            continue
        else:
            break
        
    #check for tie game
    if board.tie_game():
        print("\nTie Game\n")
        play_again = input("Play again? (y/n) > ")
        if play_again == "y":
            board.reset_board()
            continue
        else:
            break