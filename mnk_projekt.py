import numpy as np
import random
import time
import math
from datetime import datetime
import csv
from copy import deepcopy


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

    # def d_line_rd(self, start_position): # \
    #     placements = []
    #     for i in range(self.k):
    #         placement = [start_position[0] + i, start_position[1] + i]
    #         placements.append(placement)
    #     return placements
    
    # def d_line_ld(self, start_position): # /
    #         placements = []
    #         for i in range(self.k):
    #             placement = [start_position[0] + i, start_position[1] - i]
    #             placements.append(placement)
    #             # print(f"{i}: {placement}")
    #         return placements

    # def place_line_rd(self, bg, line_var):
    #     """input, array, m, n, k, and the variable that we're searching for
    #     makes a mask in the top right, k away form the far edge and bottom because only there are possible starting points
    #     """
    #     # print(arr)
    #     temp_board = np.copy(self.board)
    #     temp_board[:, -(k-1):] = 0
    #     temp_board[-(k-1):, :] = 0
    #     # print(arr)
    #     past_moves = np.argwhere(temp_board == self.current_player)

    #     # place \ line
    #     # only relevant starting positions are in the top left corner
    #     # k distance from the right side, and the bottom
    #     possible_lines = []
    #     for i in range(len(past_moves)):
    #         line_rd = self.d_line_rd(past_moves[i])
    #         zero_mask = np.full((self.board.shape[0], self.board.shape[1]), bg, dtype=int)
    #         for coord in line_rd:
    #             # print(coord[0], coord[1])
    #             zero_mask[(coord[0], coord[1])] = line_var
    #         possible_lines.append(zero_mask)
    #     return possible_lines

    # def place_line_ld(self, bg, line_var):
    #     """input, array, m, n, k, and the variable that we're searching for
    #     makes a mask in the top right, k away form the far edge and bottom because only there are possible starting points
    #     """
    #     print(self.board)
    #     temp_board = np.copy(self.board)
    #     temp_board[:, :(k-1)] = 0
    #     temp_board[-(k-1):, :] = 0
    #     print(self.board)
    #     past_moves = np.argwhere(temp_board == self.current_player)

    #     # place \ line
    #     # only relevant starting positions are in the top left corner
    #     # k distance from the right side, and the bottom
    #     possible_lines = []
    #     for i in range(len(past_moves)):
    #         line_rd = self.d_line_ld(past_moves[i])
    #         zero_mask = np.full((self.board.shape[0], self.board.shape[1]), bg, dtype=int)
    #         for coord in line_rd:
    #             # print(coord[0], coord[1])
    #             zero_mask[(coord[0], coord[1])] = line_var
    #         possible_lines.append(zero_mask)
    #     return possible_lines

    # def has_won(self, current_player, k):
    #     """_summary_
    #     playerX has won when there is a k-long Pattern on the m x n board
    #     start checking for winning pattern after k moves
    #     !! checking diagonally misses
    #     made by Dalia
    #     """
    #     self.current_player = current_player

    #     # check for rows
    #     for row in range(self.m): # changed from n to m to check last row!
    #         # also changed labels row <-> col
    #         count = 0
    #         for col in self.board.T:
    #             if col[row] == current_player:
    #                 count += 1
    #                 if count == k:
    #                     return True
    #             else:
    #                 count = 0

    #     # check the columns
    #     for col in range(self.n):
    #         count = 0
    #         for row in self.board:
    #             if row[col] == current_player:
    #                 count += 1
    #                 if count == k:
    #                     return True
    #             else:
    #                 count = 0
        
    #     # check for diagonals
    #     # The Process:
    #                 # make an array filled with 0 and a k long line of ones for every player_number
    #                 # multiply the game board with this mask
    #                 # add this mask to an array filled with the player number an 0s where the diagonal line is
    #                 # if all entries are the same, return True
    #                 # else return False or None, if no line is detected
    #     # \
    #     list_of_lines_rd = self.place_line_rd(bg=0, line_var=1)
    #     list_of_inverse_lines_w_player_number_rd = self.place_line_rd(bg=self.current_player, line_var=0)
        
    #     for i in range(len(list_of_lines_rd)):
    #         comparison_step_1_rd = list_of_lines_rd[i] * self.board
    #         comparison_step_2_rd = comparison_step_1_rd + list_of_inverse_lines_w_player_number_rd[i]
    #         all_same = np.all(comparison_step_2_rd==self.current_player)
    #         if all_same:
    #             return True
    #         else:
    #             pass

    #     list_of_lines_ld = self.place_line_rd(bg=0, line_var=1)
    #     list_of_inverse_lines_w_player_number_ld = self.place_line_rd(bg=self.current_player, line_var=0)
        
    #     for i in range(len(list_of_lines_ld)):
    #         comparison_step_1_ld = list_of_lines_ld[i] * self.board
    #         comparison_step_2_ld = comparison_step_1_rd + list_of_inverse_lines_w_player_number_ld[i]
    #         all_same = np.all(comparison_step_2_ld==self.current_player)
    #         if all_same:
    #             return True
    #         else:
    #             pass
        

    #     # check for diagonal k long lines - Anton
    #     # diagonal nach links
    #     # wie beschreibt man eine linie die k lang ist und diagonal?
    #     # starting point kann nur im bereich [m, m-k][n, n-k]
    #     return False
    
    def has_won(self, player):
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
        returns list of all available moves on the board, only used for Bot_MCTS
        """
        available_moves = []
        # Iterate over the board to find empty spaces
        for row_index, row in enumerate(self.board):
            for col_index, value in enumerate(row):
                if value == 0:  # If the space is empty
                    available_moves.append((row_index, col_index))
        return available_moves
    
    def full_board(self):
        # goes through each row and checks if value of every cell is 0
        for row in self.board:
            for value in row:
                if value == 0:
                    return False  # Found an empty cell, so the board is not full
        return True  # No empty cells were found, the board is full

class Player():

    def __init__(self, player_number, name, board) -> None: # player number 1 or 2
        self.name = name
        self.player_number = player_number
        self.board = board
        self.player_type = "human"


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

    # !! man kann nur einen value error causen, bevor das Spiel abbricht :(
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
        self.player_type = "bot_random"

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
        self.player_type = "bot_simple"
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


class Bot_complex(Player):

    def __init__(self, player_number, name, board) -> None:
        super().__init__(player_number, name, board)
        self.player_type = "bot_complex"

    def make_move(self): # -> (row, col)
        pass

class Bot_MCTS(Player):

    def __init__(self, player_number, name, board):
        super().__init__(player_number, name, board)
        self.player_type = "bot_MCTS"

        # Additional initialization specific to MCTS if needed
    
    def simulate_random_playthrough(self, board, current_player):
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
 

    def __init__(self, m=6, n=7, k=4, player1=None, player2=None):
        self.m = m
        self.n = n
        self.k = k
        self.player1 = player1
        self.player2 = player2   
        self.board = None

    def game_log(self):
        """ # Main Game Log:
        adds entry to dp (.csv) looking like this:

        | player1_type | player2_type | starting_player | winning_player | {self.m}x{self.n}_final_board_flat |
        |--------------|--------------|-----------------|----------------|------------------------------------|
        | player       | player       | 1               | 0              | 8                                  |
        | bot_random   | bot_random   | 2               | 1              | 9                                  |
        | bot_simple   | bot_simple   | 1               | 2              | 12                                 |
        | bot_complex  | bot_complex  | 2               | 0              | 16                                 |
        """
        with open("game_log.csv", mode='a', newline="") as f:
            fieldnames = ["player1_type", "player2_type", "starting_player", "winning_player", f"{self.m}x{self.n}_final_board_flat"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if f.tell() == 0:
                writer.writeheader()
            
            writer.writerow({"player1_type": self.player1.player_type,
                             "player2_type": self.player2.player_type,
                             "starting_player": self.starting_player,
                             "winning_player": self.winning_player,
                             f"{self.m}x{self.n}_final_board_flat": self.board.board.flatten()})
            f.close()


    def player_choice(self, p_number:int, p_name:str, choice:int):
        valid_choices = [1, 2, 3, 4] 

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
                player = Bot_MCTS(p_number, p_name, self.board)
                return player
            else:
                raise ValueError("input number out of range, please retry!")

    
    def start(self, player1_type, player1_name, player2_type, player2_name):    
        self.board = Board(self.m, self.n, self.k)


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
        # made by Dalia
        # current_player = random.choice([self.player1, self.player2])
        # changed for diagonal testing to:
        current_player = self.player1
        self.starting_player = current_player
        

        while not self.full_board() and not self.board.has_won(current_player):

            if np.all(self.board == 0):
                print("uyoasildgjkfbhvagluihsdkjf")
                self.starting_player = current_player
            self.board.display()
            # print(self.board.get_available_moves())
            print(f"Player {current_player.name}'s turn")
            # gets the current move the player inputed
            current_move = current_player.make_move()
            
            # puts the move on the board
            self.board.board[current_move] = current_player.player_number
            
            # checks if someone has won and if the board is full
            if self.board.has_won(current_player.player_number):
                print(f"Player {current_player.name} wins!")
                self.winning_player = current_player.player_number
                break
            elif self.full_board():
                print('The board is full. Nobody won!')
                self.winning_player = 0
                break

            # changes player
            if current_player == self.player1:
                current_player = self.player2
            else:
                current_player = self.player1

            time.sleep(0.5)

        self.board.display()

if __name__ == "__main__":

    m = 5
    n = 5
    k = 4

    # simple v mcts
    # for a in range(1000):
    #     current_game = Game(m, n, k)
    #     # human : 1, bot random: 2, bot simple: 3, bot complex: 4
    #     current_game.start(player1_type=3, player1_name="simple_1",
    #                        player2_type=4, player2_name="monte_carlo_tree_search")
    #     current_game.game_loop()
    #     current_game.game_log()

    # # simple v random
    # for d in range(1000):
    #     current_game = Game(m, n, k)
    #     # human : 1, bot random: 2, bot simple: 3, bot complex: 4
    #     current_game.start(player1_type=3, player1_name="simple_1",
    #                        player2_type=2, player2_name="random")
    #     current_game.game_loop()
    #     current_game.game_log()

    # # mcts v simple  MISSINGGGGGG
    # for b in range(998):
    #     current_game = Game(m, n, k)
    #     # human : 1, bot random: 2, bot simple: 3, bot complex: 4
    #     current_game.start(player2_type=3, player2_name="simple_1",
    #                        player1_type=4, player1_name="monte_carlo_tree_search")
    #     current_game.game_loop()
    #     current_game.game_log()

    # # mcts v random
    # for c in range(1000):
    #     current_game = Game(m, n, k)
    #     # human : 1, bot random: 2, bot simple: 3, bot complex: 4
    #     current_game.start(player2_type=2, player2_name="random",
    #                        player1_type=4, player1_name="monte_carlo_tree_search")
    #     current_game.game_loop()
    #     current_game.game_log()

    # random v simple
    for d in range(900):
        current_game = Game(m, n, k)
        # human : 1, bot random: 2, bot simple: 3, bot complex: 4
        current_game.start(player1_type=2, player1_name="random",
                           player2_type=3, player2_name="simple_1")
        current_game.game_loop()
        current_game.game_log()

    # random v mcts
    for d in range(1000):
        current_game = Game(m, n, k)
        # human : 1, bot random: 2, bot simple: 3, bot complex: 4
        current_game.start(player1_type=2, player1_name="random",
                           player2_type=4, player2_name="monte_carlo_tree_search")
        current_game.game_loop()
        current_game.game_log()