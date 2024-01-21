import numpy as np

array = np.array([[0, 1, 0, 0, 0],
                  [0, 2, 0, 0, 0],
                  [1, 0, 2, 1, 0],
                  [0, 0, 1, 2, 1],
                  [0, 1, 0, 0, 2],
                  [1, 2, 2, 0, 0]])

# the approach below works?? but is doesn't???
"""
def diagonal_line_TF(arr, start_position, k):
    placement_list = []
    for i in range(k): # replace with winning length
        if start_position > 15: # need to find a formula that scales this variable dynamically to the game board
            break
        else:
            x = np.take(arr, i+start_position)
            start_position += 3 # self.board.m -2 num cols on board /
            # start_position += 5 # self.board.m num cols on board \
            placement_list.append(x)
        
    for i in range(k): # replace with winning length
        if start_position > 12: # need to find a formula that scales this variable dynamically to the game board
            break
        else:
            x = np.take(arr, i+start_position)
            # start_position += 3 # self.board.m -2 num cols on board /
            start_position += 5 # self.board.m num cols on board \
            placement_list.append(x)
    
    all_same = all(x==placement_list[0] for x in placement_list)
    return all_same

def past_move_cords_to_position(past_moves, m, n):
    start_positions = []
    num_moves = past_moves.shape[0]
    for i in range(num_moves):
        one_position = n * past_moves[i][0] + past_moves[i][1] + 1
        start_positions.append(one_position)
    return start_positions



m, n = (6, 5)
var = 4
past_moves = np.argwhere(array == var)

start_positions = past_move_cords_to_position(past_moves, m, n)

for i in range(len(start_positions)):
    true_false = diagonal_line_TF(array, start_positions[i], 4)
    if true_false:
        print("found diagonal line!")
        break
    else:
        print("didnt find a line :(")
"""


# new apporach:
# make an array filled with 0 and a k long diagonal line of ones.. done
# add multiply the game board with this mask
# add this mask to an array filled with the player number and 0 where the diagonal line is
# if all entries in the array are the same, the diagonal line was a winning line
# if not, shift array mask and try again

# has to be done for \ and / lines!

def d_line_rd(start_position, k): # \
    
    placements = []
    for i in range(k):
        placement = [start_position[0] + i, start_position[1] + i]
        placements.append(placement)
    return placements

def d_line_ld(start_position, k): # /
    placements = []
    for i in range(k):
        placement = [start_position[0] + i, start_position[1] - i]
        placements.append(placement)
        print(f"{i}: {placement}")
    return placements

def place_line_rd(arr, m, n, k, var, bg, line_var):
    """input, array, m, n, k, and the variable that we're searching for
    makes a mask in the top right, k away form the far edge and bottom because only there are possible starting points
    """
    print(arr)
    arr[:, -(k-1):] = 0
    arr[-(k-1):, :] = 0
    print(arr)
    past_moves = np.argwhere(arr == var)
    
    # place \ line
    # only relevant starting positions are in the top left corner
    # k distance from the right side, and the bottom
    possible_lines = []
    for i in range(len(past_moves)):
        line_rd = d_line_rd(past_moves[i], k)
        zero_mask = np.full((arr.shape[0], arr.shape[1]), bg, dtype=int)
        for coord in line_rd:
            print(coord[0], coord[1])
            zero_mask[(coord[0], coord[1])] = line_var
        possible_lines.append(zero_mask)
    return possible_lines

def has_won(game_board, list_of_lines, list_of_inverse_lines_w_player_number, player_number):
    for i in range(len(list_of_lines)):
        print(game_board)
        comparison_step_1 = list_of_lines[i] * game_board
        print(comparison_step_1)
        comparison_step_2 = comparison_step_1 + list_of_inverse_lines_w_player_number[i]
        print(comparison_step_2)
        all_same = np.all(comparison_step_2==player_number)
        return all_same
    

m, n ,k = (6, 5, 4)
var = 1

possible_lines = place_line_rd(array, m, n, k, var, 0, line_var=1)
inverse_possible_lines_w_player_number = place_line_rd(array, m, n, k, var, var, line_var=0)
print(possible_lines)
print(inverse_possible_lines_w_player_number)

array = np.array([[0, 1, 0, 0, 0],
                  [0, 2, 0, 0, 0],
                  [1, 0, 2, 1, 0],
                  [0, 0, 1, 2, 1],
                  [0, 1, 0, 0, 2],
                  [1, 2, 2, 0, 0]])

print(has_won(array, possible_lines, inverse_possible_lines_w_player_number, player_number=var))