# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:49:58 2024

@author: Dalia Salih

mnk_projekt aber auf GUI kompatibel
"""

import numpy as np
import random
import time
import math
from datetime import datetime
import csv
from copy import deepcopy


class Board():
<<<<<<< Updated upstream

    def __init__(self, m, n, k) -> None:
=======
    """
    Represents the game board for an m*n*k game, 
    where m*n is the dimension of the board and k is the winning sequence length.
    """
    def __init__(self, m, n, k) -> None:
        """
        Initialize the game board with the specified dimensions and winning sequence length.

        Parameters:
        - m (int): Number of rows in the game board.
        - n (int): Number of columns in the game board.
        - k (int): Length of the sequence needed to win the game.

        Raises:
        - ValueError: If k is larger than either dimension of the board, 
        throwing an error due to game logic constraints.
        """
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
        """
        Prints the current state of the game board to the console.
        """
>>>>>>> Stashed changes
        print(self.board)
        
    
    def place_move(self, row, col, current_player):
<<<<<<< Updated upstream
=======
        """
        Attempts to place a move on the board for the current player.

        Parameters:
        - row (int): The row index for the move.
        - col (int): The column index for the move.
        - current_player (Player): The player making the move.

        Returns:
        - bool: True if the move was successfully placed, False otherwise.
        """
>>>>>>> Stashed changes
        if current_player is None or not isinstance(current_player, (Player)):
            print(f"Invalid player number: {current_player}")
            return False
    # First, check if the chosen position is within the bounds of the board
        if 0 <= row < self.m and 0 <= col < self.n:
            # Then, check if the selected cell is empty (0)
            if self.board[row, col] == 0:
                self.board[row, col] = current_player.player_number
                return True
            else:
                print("This cell is already taken. Please choose a different cell.")
                return False
        else:
            print("Invalid move. Please choose a cell within the board's bounds.")
            return False

    def full_board(self):
<<<<<<< Updated upstream
        # made by Dalia
        # goes through row and checks if value of every cell is 0
=======
        """
        Checks if the board is completely filled with no empty spaces.

        Returns:
        - bool: True if the board is full, False otherwise.
        """
>>>>>>> Stashed changes
        for row in self.board:
            for value in row:
                if value == 0:
                    return False
        return True

    def has_won(self, player):
<<<<<<< Updated upstream
=======
        """
        Checks if the specified player has won the game.

        Parameters:
        - player (int): The player number to check for a win condition.

        Returns:
        - bool: True if the player has won, False otherwise.
        """
>>>>>>> Stashed changes
        # Horizontal check
        for row in range(self.m):
            for col in range(self.n - self.k + 1):
                if all(self.board[row][c] == player for c in range(col, col + self.k)):
                    return True
        # Vertical check
        for row in range(self.m - self.k + 1):
            for col in range(self.n):
                if all(self.board[r][col] == player for r in range(row, row + self.k)):
                    return True
        # Diagonal check (down-right)
        for row in range(self.m - self.k + 1):
            for col in range(self.n - self.k + 1):
                if all(self.board[row + d][col + d] == player for d in range(self.k)):
                    return True
        # Diagonal check (down-left)
        for row in range(self.m - self.k + 1):
            for col in range(self.k - 1, self.n):
                if all(self.board[row + d][col - d] == player for d in range(self.k)):
                    return True
        return False
    
    def get_available_moves(self):
        """
<<<<<<< Updated upstream
        returns list of all available moves on the board, only used for Bot_MCTS
=======
        Retrieves a list of all available moves on the board.

        Returns:
        - list of tuples: Each tuple represents an available move as (row, col).
>>>>>>> Stashed changes
        """
        available_moves = []
        # Iterate over the board to find empty spaces
        for row_index, row in enumerate(self.board):
            for col_index, value in enumerate(row):
                if value == 0:  # If the space is empty
                    available_moves.append((row_index, col_index))
        return available_moves

class Player():
<<<<<<< Updated upstream

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
=======
    """
    Represents a human player in the mnk-game.
    """

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        """
        Initialize a human player with a specific name and player number.

        Parameters:
        - player_number (int): The number identifying the player (1 or 2).
        - name (str): The name of the player.
        - board (Board): The game board instance.
        """
>>>>>>> Stashed changes
        self.name = name
        self.player_number = player_number
        self.board = board
        self.player_type = "human"


    def is_valid(self, move:tuple):
<<<<<<< Updated upstream
        '''
        erhält ein tuple von moves
        prüft ob moves in valid raum ist
        gibt true or false wieder

        '''

=======
        """
        Determines if the chosen move is valid (i.e., within the bounds of the board and on an empty cell).

        Parameters:
        - move (tuple): The desired move location (row, col).

        Returns:
        bool: True if the move is valid, False otherwise.
        """
>>>>>>> Stashed changes
        # checks if move is in range of the size of the board
        if move[0] < self.board.m and move[1] < self.board.n:
            print(self.board)
            # checks the cell that is to be changed is == 0
            if self.board.board[move[0]][move[1]] == 0:
                return True
        else:
            return False

<<<<<<< Updated upstream
    # !! man kann nur einen value error causen, bevor das Spiel abbricht :(
    def make_move(self): # -> (row, col)
=======

    def make_move(self): # -> (row, col)
        """
        Handles receiving a player's move via input and validating it.

        Returns:
        tuple: The coordinates (row, col) of the player's move.
        """
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream

    def __init__(self, player_number, name, board) -> None:
=======
    """
    A bot player that selects moves randomly. Inherits behavior from Player.
    """

    def __init__(self, player_number, name, board) -> None:
        """
        Initialize a bot player that moves randomly.
        Parameters are inherited from Player class.
        """
>>>>>>> Stashed changes
        super().__init__(player_number, name, board)
        self.player_type = "bot_random"

    def make_move(self): # -> (row, col)
        """
<<<<<<< Updated upstream
        geht in eine schleife und wiederholt die erzeugung vom random move so lange bis es valid ist
        made by Dalia
        """

=======
        Generates and validates a random move until a legal move is found.
        Returns:
        tuple: The coordinates (row, col) of the chosen move.
        """
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    
    def __init__(self, player_number, name, board) -> None:
=======
    """
    A bot player that attempts to place its markers strategically with a simple set of rules.
    Inherits behavior from Player.
    """
    def __init__(self, player_number, name, board) -> None:
        """
        Initialize a simple strategy bot player.
        Parameters are inherited from Player class.
        """
>>>>>>> Stashed changes
        super().__init__(player_number, name, board)
        self.player_type = "bot_simple"
        pass


    def make_move(self): # -> (row, col)
        """
<<<<<<< Updated upstream
        goal of this bot: only try and win (be better than random bot)
        if the board is empty, place an entry k/2 away from the edges
            placed @ (m_i, n_i)
        if there is one placed entry, pick a random neighboring entry to fill
            placed @ (m_i+-1, n_i+-1)
        if there are two in line, continue along that line
=======
        Implements a simple strategy for choosing moves with the goal of winning or improving its position.
        Returns:
        tuple: The coordinates (row, col) of the chosen move.
>>>>>>> Stashed changes
        """
        valid_move = True
        valid_counter = 1
        while valid_move:
            # stage one
            if self.player_number not in self.board.board[:, :]:#not np.any(self.board.board[:, :] == self.player_number):
                # print("in for loop for first placement")
                distance_from_edge = math.floor(self.board.k/2) # halves wining length, rounds down if k/2 is a float
                move = (random.randint(distance_from_edge - 1, self.board.m - 1 - distance_from_edge),
                        random.randint(distance_from_edge - 1, self.board.n - 1 - distance_from_edge))
            #stage two
            elif self.player_number in self.board.board[:, :] and np.argwhere(self.board.board == self.player_number).shape[0] == 1: # goes here if theres 1 or more

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
            # stage 3
            else:
                # what is a line in an array
                # v_line: (m_i, n_i) ... (m_i, n_i+k)
                # h_line: (m_i, n_i) ... (m_i+k, n_i)
                # d_line_1: (m_i, n_i) ... (m_i+k, n_i+k)
                # d_line_2: (m_i, n_i) ... (m_i+k, n_i-k)
                # using np.argwhere gets the coord for each placed entry
                # finds line checking if one of the four sum funcs above would apply.

                past_moves = np.argwhere(self.board.board == self.player_number)

                # when valid counter is too high place a random move
                if valid_counter > 5:
                    move = (random.randint(0, self.board.m - 1),
                            random.randint(0, self.board.n - 1))
                    print("stuck in random after valid_counter overflow")
                
                # find h_line
                elif np.all(past_moves[:, 0] == past_moves[0, 0]):
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
                # find / line and \ line
                # causes problem, because the bot can choose 4 positions...
                # 
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
<<<<<<< Updated upstream

    def __init__(self, player_number, name, board) -> None:
=======
    """
    An enhanced version of Bot_simple with a different set of strategies for choosing moves.
    Inherits behavior from Player.
    """
    def __init__(self, player_number, name, board) -> None:
        """
        Initialize an enhanced simple strategy bot player.
        Parameters are inherited from Player class.
        """
>>>>>>> Stashed changes
        super().__init__(player_number, name, board)
        self.player_type = "bot_simple_2"
        pass
    
    def make_move(self): # -> (row, col)
        """
<<<<<<< Updated upstream
        goal of this bot: try to win
        if empty, place an entry in the middle of the board
        if there is an entry already, bot will find position of its own entry and place an entry next to/ above/ below it
        else place an entry randomly
=======
        Implements an enhanced strategy over Bot_simple for choosing moves, 
        including center placement and adjacency strategies.
        Returns:
        tuple: The coordinates (row, col) of the chosen move.
>>>>>>> Stashed changes
        """
        valid_move = True
        while valid_move:
            if self.board.board[self.board.m//2, self.board.n//2] == 0:
                move = ((self.board.m//2), (self.board.n//2))         #if middle of the board is empty, place an entry
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
<<<<<<< Updated upstream

    def __init__(self, player_number, name, board) -> None:
=======
    """
    Implements a bot player that uses Monte Carlo Tree Search (MCTS) for decision-making.
    Inherits behavior from Player.
    """

    def __init__(self, player_number, name, board) -> None:
        """
        Initialize a MCTS bot player.
        Parameters are inherited from Player class.
        """
>>>>>>> Stashed changes
        super().__init__(player_number, name, board)
        self.player_type = "bot_complex"

        # Additional initialization specific to MCTS if needed
    
    def simulate_random_playthrough(self, board, current_player):
<<<<<<< Updated upstream
=======
        """
        Simulates a random playthrough from the current state to determine the potential outcome of a move.

        Parameters:
        - board (Board): The current state of the game board.
        - current_player (int): The player number of the current player.

        Returns:
        int: The outcome of the simulation (1 for win, -1 for loss, 0 for draw).
        """
>>>>>>> Stashed changes
        temp_board = deepcopy(board)  # Use a deep copy to avoid mutating the original
        moves = temp_board.get_available_moves()
        np.random.shuffle(moves)  # Randomly shuffle available moves to avoid bias

        while moves:
            move = moves.pop()
            temp_board.board[move[0]][move[1]] = current_player
            if temp_board.has_won(current_player):
                return 1 if current_player == self.player_number else -1
            elif temp_board.full_board():
                return 0
            current_player = 3 - current_player  # Switch players

        return 0

    def make_move(self):
<<<<<<< Updated upstream
=======
        """
        Uses MCTS to choose the most promising move based on simulations of possible outcomes.

        Returns:
        tuple: The coordinates (row, col) of the chosen move.
        """
>>>>>>> Stashed changes
        available_moves = self.board.get_available_moves()
        move_scores = {move: 0 for move in available_moves}
        
        for move in available_moves:
            for _ in range(100):  # Conduct 100 simulations for each available move
                temp_board = deepcopy(self.board)
                temp_board.board[move[0]][move[1]] = self.player_number
                result = self.simulate_random_playthrough(temp_board, 3 - self.player_number)
                move_scores[move] += result
        
        # Randomize selection among top-scoring moves if there's a tie
        max_score = max(move_scores.values())
        best_moves = [move for move, score in move_scores.items() if score == max_score]
        best_move = random.choice(best_moves)  # Randomly choose among the best if there's a tie

        # Apply the chosen move to the actual board
        self.board.board[best_move[0]][best_move[1]] = self.player_number
        return best_move


class Game():
<<<<<<< Updated upstream


    def __init__(self, m=6, n=7, k=4, player1=None, player2=None):
=======
    """
    Manages the gameplay and interactions between two players in the mnk-game.
    """

    def __init__(self, m=6, n=7, k=4, player1=None, player2=None):
        """
        Initialize the game with specified dimensions and players.

        Parameters:
        - m (int): Number of rows on the game board.
        - n (int): Number of columns on the game board.
        - k (int): Consecutive symbols needed to win.
        - player1 (Player): The first player.
        - player2 (Player): The second player.
        """
>>>>>>> Stashed changes
        self.m = m
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2   
        self.board = None
        self.starting_player = None
        self.current_player = None
        
        self.saved_player1_type = None
        self.saved_player1_name = None
        self.saved_player2_type = None
        self.saved_player2_name = None
        
        
    def game_log(self):
        """ # Main Game Log:
<<<<<<< Updated upstream
        adds entry to dp (.csv) looking like this:

=======
        Records the outcomes and key game information to a .csv file for historical analysis.
>>>>>>> Stashed changes
        | player1_type | player2_type | starting_player | winning_player |
        |--------------|--------------|-----------------|----------------|
        | player       | player       | 1               | 0              |
        | bot_random   | bot_random   | 2               | 1              |
        | bot_simple   | bot_simple   | 1               | 2              |
        | bot_complex  | bot_complex  | 2               | 0              |
        """
        with open("game_log.csv", mode='a', newline="") as f:
            fieldnames = ["player1_type", "player2_type", "starting_player", "winning_player"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            
            writer.writerow({"player1_type": self.player1.player_type,
                              "player2_type": self.player2.player_type,
                              "starting_player": self.starting_player,
                              "winning_player": self.winning_player})
            f.close()

    def player_choice(self, p_number:int, p_name:str, choice:int):
<<<<<<< Updated upstream
=======
        """
        Initializes and returns a player object based on the choice provided.

        Parameters:
        - p_number (int): The player's number (1 or 2).
        - p_name (str): The player's name.
        - choice (int): The numeral choice that corresponds to the type of player (e.g., human, bot).

        Returns:
        Player: An instantiated player of the chosen type.
        """
>>>>>>> Stashed changes
        valid_choices = [1, 2, 3, 4, 5] 
        if choice in valid_choices:
            if choice == 1:
                player = Player(p_number, p_name, self.board)
                return player
            elif choice == 2:
                player = Bot_random(p_number, p_name, self.board)
                return player
            elif choice == 3:
                player = Bot_simple(p_number, p_name, self.board)
                return player
            elif choice == 4:
                player = Bot_simple_v2(p_number, p_name, self.board)
                return player
            elif choice == 5:
                player = Bot_complex(p_number, p_name, self.board)
                return player
            else:
                print(f"Invalid player type: {choice}")
                raise ValueError(f"Invalid player type: {choice}")
    
<<<<<<< Updated upstream
    def start(self, player1_type, player1_name, player2_type, player2_name):    
=======
    def start(self, player1_type, player1_name, player2_type, player2_name):   
        """
        Starts a new game session with the specified player types and names.

        Parameters:
        - player1_type (int): The type of player 1.
        - player1_name (str): The name of player 1.
        - player2_type (int): The type of player 2.
        - player2_name (str): The name of player 2.
        """
>>>>>>> Stashed changes
        self.board = Board(self.m, self.n, self.k)

        self.player1 = self.player_choice(1, player1_name, player1_type)
        self.player2 = self.player_choice(2, player2_name, player2_type)
        print(f'player1: {self.player1}, player2: {self.player2}')
        self.current_player = random.choice([self.player1, self.player2]) 
        
        self.save_game_details(player1_type, player1_name, player2_type, player2_name)

    def restart_game(self):
<<<<<<< Updated upstream
        """Restart the game using saved player details and board dimensions."""
=======
        """
        Restarts the game using saved player details and board dimensions.
        """
>>>>>>> Stashed changes
        if self.saved_player1_type is not None and self.saved_player2_type is not None:
            self.start(self.saved_player1_type, self.saved_player1_name, 
                       self.saved_player2_type, self.saved_player2_name)
        else:
            print("Game details not found. Cannot restart.")
            
    def save_game_details(self, player1_type, player1_name, player2_type, player2_name):
<<<<<<< Updated upstream
        """Save player types, names, and board dimensions for game restart."""
=======
        """
        Saves the current game's player types and names for potential restart.

        Parameters:
        - player1_type (int): The type of player 1.
        - player1_name (str): The name of player 1.
        - player2_type (int): The type of player 2.
        - player2_name (str): The name of player 2.
        """
>>>>>>> Stashed changes
        self.saved_player1_type = player1_type
        self.saved_player1_name = player1_name
        self.saved_player2_type = player2_type
        self.saved_player2_name = player2_name

    def switch_player(self):
        print(f"Switching player from {self.current_player}")
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        print(f"New current player is {self.current_player}")
    
    def place_move(self, position):
<<<<<<< Updated upstream
=======
        """
        Attempts to place a move on the board for the current player.

        Parameters:
        - position (tuple): The desired move position as (row, col).

        Returns:
        - tuple: A tuple containing a boolean indicating if the move was successful, and a message string.
        """
>>>>>>> Stashed changes
        row, col = position
        successful_move = self.board.place_move(row, col, self.current_player)
        if successful_move:
            if self.board.has_won(self.current_player):
                return True, f"Player {self.current_player} wins!"
            
            return True, None  # Move was successful but no win
    
        return False, "Invalid move, try again."
        
    def get_current_player(self):
<<<<<<< Updated upstream
=======
        """
        Retrieves the current player object.

        Returns:
        - Player: The current player object.
        """
>>>>>>> Stashed changes
        print(f"get_current_player: {self.current_player}, Type: {type(self.current_player)}")
        if self.current_player == 1:
            return self.player1
        elif self.current_player == 2:
            return self.player2
        # Correctly return the current player object
        return self.current_player


if __name__ == "__main__":
    for i in range(1000):
        # for testing the script w/o gui and user input:
        m = 6
        n = 5
        k = 4   

        current_game = Game(m, n, k)
        # human : 1, bot random: 2, bot simple: 3, bot complex: 4
        current_game.start(player1_type=3, player1_name="simple",
                           player2_type=2, player2_name="random")
        current_game.game_loop()
        current_game.game_log() # pretty please pretty dalia add this to the gui :*.... or else >:(