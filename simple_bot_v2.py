import numpy as np
import random
import time
import math
from datetime import datetime


class Board():

    def __init__(self, m, n, k) -> None:
        self.m = m
        self.n = n
        self.k = k

        # check if zielgerade is larger than gameboard
        if self.m < self.k:
            raise ValueError("k can't be larger than n or m")
        elif self.n < self.k:
            raise ValueError("k can't be larger than n or m")
        else:
            self.board = np.zeros(shape=(self.m, self.n), dtype=int)

        return

    def display(self):
        print(self.board)

    def has_won(self, current_player, k):
        """_summary_
        playerX has won when there is a k-long Pattern on the m x n board
        start checking for winning pattern after k moves

        !! checking diagonally misses
              made by Dalia
        """

        self.current_player = current_player

        # check for rows
        for col in range(self.n):
            count = 0
            for row in self.board.T:
                if row[col] == current_player:
                    count += 1
                    if count == k:
                        return True
                else:
                    count = 0

        # check the columns
        for col in range(self.n):
            count = 0
            for row in self.board:
                if row[col] == current_player:
                    count += 1
                    if count == k:
                        return True
                else:
                    count = 0
                         
        return False



class Player():

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        self.name = name
        self.player_number = player_number
        self.board = board


    def is_valid(self, move:tuple):
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder

        '''

        # checks if move is in range of the size of the board
        if move[0] < self.board.m and move[1] < self.board.n:
            print(self.board)
            # checks the cell that is to be changed is == 0
            if self.board.board[move[0]][move[1]] == 0:
                return True
        else:
            return False


    def make_move(self): # -> (row, col)
        print(f"make move between 0 and {self.board.m-1} \nand 0 and {self.board.n-1}")
        try: move = (int(input("Please make a move: ")), int(input("")))
        except ValueError:
            print("Sorry please put an integer")
        move = (int(input("Please make a move: ")), int(input("")))
        while not self.is_valid(move):
            print('Invalid move. Please try again')
            move = (int(input("Please make a move: ")), int(input("")))
        return move
        

class Bot_random(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)


    def make_move(self): # -> (row, col)
        """
        geht in eine schleife und wiederholt die erzeugung vom random move so lange bis es valid ist
        made by Dalia
        """

        realitycheck = True
        while realitycheck:
            move = (random.randint(0, self.board.m - 1), random.randint(0, self.board.n - 1))
            if self.is_valid(move):
                realitycheck = False
               # move = (random.randint(0, self.board.m - 1), random.randint(0, self.board.n - 1))
                self.board.board[move[0]][move[1]] = self.player_number
                return move
            else:
                print('Invalid move. Please try again')

class Bot_simple(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass


    def make_move(self): # -> (row, col)
        """
        goal of this bot: only try and win (be better than random bot)
        if the board is empty, place an entry k/2 away from the edges
            placed @ (m_i, n_i)
        if there is one placed entry, pick a random neighboring entry to fill
            placed @ (m_i+-1, n_i+-1)
        if there are two in line, continue along that line
        """
        valid_move = True
        valid_counter = 1
        while valid_move:
            # stage one
            if self.player_number not in self.board.board[:, :]:#not np.any(self.board.board[:, :] == self.player_number):
                # print("in for loop for first placement")
                distance_from_edge = math.floor(self.board.k/2) # halves wining length, rounds down if k/2 is a float
                move = (random.randint(0 + distance_from_edge, self.board.m - 1 - distance_from_edge),
                        random.randint(0 + distance_from_edge, self.board.n - 1 - distance_from_edge))
                # print(move)
            #stage two
            elif self.player_number in self.board.board[:, :] and np.argwhere(self.board.board == self.player_number).shape[0] == 1: # goes here if theres 1 or more atm, should only go here if theres 1!
                # print("in loop for second placement")
                # print("\n", np.argwhere(self.board.board == self.player_number), "\n")

                first_move = (np.argwhere(self.board.board == self.player_number)[0, 0],
                              np.argwhere(self.board.board == self.player_number)[0, 1])

                # print(first_move)

                original_move = False
                while not original_move:
                    move = (random.randint(first_move[0] - 1, first_move[0] + 1),
                            random.randint(first_move[1] - 1, first_move[1] + 1))
                    # print(move)
                    if not move == first_move:
                        original_move = True

            else:
                # what is a line in an array
                # v_line: (m_i, n_i) ... (m_i, n_i+k)
                # h_line: (m_i, n_i) ... (m_i+k, n_i)
                # d_line_1: (m_i, n_i) ... (m_i+k, n_i+k)
                # d_line_2: (m_i, n_i) ... (m_i+k, n_i-k)
                # using np.argwhere gets the coord for each placed entry
                # finds line checking if one of the four sum funcs above would apply.

                past_moves = np.argwhere(self.board.board == self.player_number)
                # find h_line
                if np.all(past_moves[:, 0] == past_moves[0, 0]):
                    x_next_move = past_moves[0, 0]
                    y_next_move = random.choice([np.min(past_moves[:, 1]) - 1,
                                                 np.max(past_moves[:, 1]) + 1])
                    move = (x_next_move, y_next_move)
                # find v_line
                elif np.all(past_moves[:, 1] == past_moves[0, 1]):
                    y_next_move = past_moves[0, 1]
                    x_next_move = random.choice([np.min(past_moves[:, 0]) - 1,
                                                 np.max(past_moves[:, 0]) + 1])
                    move = (x_next_move, y_next_move)
                    print(move)
                # if no move is found, place random move
                elif valid_counter > 5:
                    move = (random.randint(0, self.board.m - 1),
                            random.randint(0, self.board.n - 1))
            
                else:
                    x_next_move = random.choice([np.min(past_moves[:, 1]) - 1,
                                                 np.max(past_moves[:, 1]) + 1])
                    y_next_move = random.choice([np.min(past_moves[:, 0]) - 1,
                                                 np.max(past_moves[:, 0]) + 1])
                    move = (x_next_move, y_next_move)

            if self.is_valid(move):
                valid_move = False
                #self.board.board[move[0]][move[1]] = self.player_number
                print(move)
                valid_counter = 0
                return move
            else:
                valid_counter += 1

        pass
    
class Bot_simple_v2(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        pass
    

    def make_move(self): # -> (row, col)
        """
        goal of this bot: try to win
        if empty, place an entry in the middle of the board
        if there is an entry already, bot will find position of its own entry and place an entry next to/ above/ below it
        else place an entry randomly
        """
        valid_move = True
        while valid_move:
            if self.board.board[m//2, n//2] == 0:
                move = ((m//2), (n//2))         #if middle of the board is empty, place an entry
            elif self.board.board[(self.board.m//2, self.board.n//2)] != 0:
                entrys_so_far = np.argwhere(self.board.board == self.player_number) #create a list with all own entrys
                position = entrys_so_far[-1]    #take position of last entry
                if position[1]+1 < (self.board.m-1) and self.board.board[position[0], position[1]+1] == 0:
                    move = (position[0], position[1]+1)
                elif position[1]-1 > (self.board.m-1) and self.board.board[position[0], position[1]-1] == 0:
                    move = (position[0], position[1]-1)                                                          #place entry next to/ above/ below last entry
                elif position[0]+1 < (self.board.n-1) and self.board.board[position[0]+1, position[1]] == 0:
                    move = (position[0]+1, position[1])
                elif position[0]-1 > (self.board.n-1) and self.board.board[position[0]-1, position[1]] == 0:
                    move = (position[0]-1, position[1])
                else:
                    move = (random.randint(0, self.board.m - 1), random.randint(0, self.board.n - 1))  #place entry somewhere on the board
            return move
        
        if self.is_valid(move):
            valid_move = False
            return move
        else:
            print('Invalid move. Please try again')
            pass


class Bot_complex(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)

    def make_move(self): # -> (row, col)
        pass
class Game():


    def __init__(self, m=6, n=7, k=4, player1=None, player2=None):
        self.m = m
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2   
        self.board = None

    def player_choice(self, p_number:int, p_name:str, choice:int):
        valid_choices = [1, 2, 3, 4]

        if choice in valid_choices:
            if choice == 1:
                player = Player(p_number, p_name, self.board)
                # print("player is human")
                # print(20*"-")
                return player
            elif choice == 2:
                player = Bot_random(p_number, p_name, self.board)
                # print("player is a random bot")
                # print(20*"-")
                return player
            elif choice == 3:
                player = Bot_simple(p_number, p_name, self.board)
                # print("player is a simple bot")
                # print(20*"-")
            elif choice == 4:
                player = Bot_simple_v2(p_number, p_name, self.board)
                # print("player is a simple bot v2")
                # print(20*"-")
                return player
            elif choice == 5:
                player = Bot_complex(p_number, p_name, self.board)
                # print("player is a complex bot")
                # print(20*"-")
                return player
            else:
                raise ValueError("input number out of range, please retry!")

    def log_moves(self):
        now = datetime.now()
        self.unique_game_id = now.strftime("%y%m%d_%H-%M-%S")

    
    def start(self, player1_type, player1_name, player2_type, player2_name):    
        self.board = Board(self.m, self.n, self.k)

        print(20*"-")
        
        self.player1 = player1_name
        self.player2 = player2_name

        self.player1 = self.player_choice(1, player1_name, player1_type)
        self.player2 = self.player_choice(2, player2_name, player2_type)

    def full_board(self):
        # made by Dalia
        # goes through row and checks if value of every cell is 0
        for row in self.board.board:
            for value in row:
                if value == 0:
                    return False
        return True

    def game_loop(self):
        #made by Dalia
        current_player = random.choice([self.player1, self.player2])
        while not self.full_board() and not self.board.has_won(current_player, self.k):
            self.board.display()
            print(f"Player {current_player.name}'s turn")
            # gets the current move the player inputed
            current_move = current_player.make_move()
            
            # puts the move on the board
            self.board.board[current_move] = current_player.player_number
            
            # checks if someone has won and if the board is full
            if self.board.has_won(current_player.player_number, self.k):
                print(f"Player {current_player.name} wins!")
                break
            elif self.full_board():
                print('The board is full. Nobody won!')
                break

            # changes player
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

            # time.sleep(0.5)

        self.board.display()
        
        
if __name__ == "__main__":
    # for testing the script w/o gui and user input:
    m = 6
    n = 5
    k = 4   

    # human : 1
    # bot random: 2
    # bot simple: 3
    # bot complex: 4
    current_game = Game(m, n, k)
    # human : 1, bot random: 2, bot simple: 3, bot simple v2: 4, bot complex: 5
    current_game.start(player1_type=4, player1_name="bot simple v2",
                       player2_type=2, player2_name="bot random")
    # human : 1, bot random: 2, bot simple: 3, bot complex: 4
    current_game.game_loop()