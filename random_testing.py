# import numpy as np

# array = np.array([[0, 1, 0, 0, 0],
#                   [0, 2, 0, 0, 0],
#                   [1, 0, 2, 1, 0],
#                   [0, 0, 1, 2, 1],
#                   [0, 1, 0, 0, 2],
#                   [1, 2, 2, 0, 0]])

# # the approach below works?? but is doesn't???
# """
# def diagonal_line_TF(arr, start_position, k):
#     placement_list = []
#     for i in range(k): # replace with winning length
#         if start_position > 15: # need to find a formula that scales this variable dynamically to the game board
#             break
#         else:
#             x = np.take(arr, i+start_position)
#             start_position += 3 # self.board.m -2 num cols on board /
#             # start_position += 5 # self.board.m num cols on board \
#             placement_list.append(x)
        
#     for i in range(k): # replace with winning length
#         if start_position > 12: # need to find a formula that scales this variable dynamically to the game board
#             break
#         else:
#             x = np.take(arr, i+start_position)
#             # start_position += 3 # self.board.m -2 num cols on board /
#             start_position += 5 # self.board.m num cols on board \
#             placement_list.append(x)
    
#     all_same = all(x==placement_list[0] for x in placement_list)
#     return all_same

# def past_move_cords_to_position(past_moves, m, n):
#     start_positions = []
#     num_moves = past_moves.shape[0]
#     for i in range(num_moves):
#         one_position = n * past_moves[i][0] + past_moves[i][1] + 1
#         start_positions.append(one_position)
#     return start_positions



# m, n = (6, 5)
# var = 4
# past_moves = np.argwhere(array == var)

# start_positions = past_move_cords_to_position(past_moves, m, n)

# for i in range(len(start_positions)):
#     true_false = diagonal_line_TF(array, start_positions[i], 4)
#     if true_false:
#         print("found diagonal line!")
#         break
#     else:
#         print("didnt find a line :(")
# """


# # new apporach:
# # make an array filled with 0 and a k long diagonal line of ones.. done
# # add multiply the game board with this mask
# # add this mask to an array filled with the player number and 0 where the diagonal line is
# # if all entries in the array are the same, the diagonal line was a winning line
# # if not, shift array mask and try again

# # has to be done for \ and / lines!

# def d_line_rd(start_position, k): # \
#     placements = []
#     for i in range(k):
#         placement = [start_position[0] + i, start_position[1] + i]
#         placements.append(placement)
#     return placements

# def d_line_ld(start_position, k): # /
#     placements = []
#     for i in range(k):
#         placement = [start_position[0] + i, start_position[1] - i]
#         placements.append(placement)
#         # print(f"{i}: {placement}")
#     return placements

# def place_line_rd(arr, m, n, k, var, bg, line_var):
#     """input, array, m, n, k, and the variable that we're searching for
#     makes a mask in the top right, k away form the far edge and bottom because only there are possible starting points
#     """
#     # print(arr)
#     mod_arr = np.copy(arr)
#     mod_arr[:, -(k-1):] = 0
#     mod_arr[-(k-1):, :] = 0
#     # print(arr)
#     past_moves = np.argwhere(mod_arr == var)
    
#     # place \ line
#     # only relevant starting positions are in the top left corner
#     # k distance from the right side, and the bottom
#     possible_lines = []
#     for i in range(len(past_moves)):
#         line_rd = d_line_rd(past_moves[i], k)
#         zero_mask = np.full((arr.shape[0], arr.shape[1]), bg, dtype=int)
#         for coord in line_rd:
#             # print(coord[0], coord[1])
#             zero_mask[(coord[0], coord[1])] = line_var
#         possible_lines.append(zero_mask)
#     return possible_lines

# def place_line_ld(arr, m, n, k, var, bg, line_var):
#     """input, array, m, n, k, and the variable that we're searching for
#     makes a mask in the top right, k away form the far edge and bottom because only there are possible starting points
#     """
#     print(arr)

#     mod_arr = np.copy(arr)
#     mod_arr[:, :(k-1)] = 0
#     mod_arr[-(k-1):, :] = 0
#     print(arr)
#     past_moves = np.argwhere(mod_arr == var)
    
#     # place \ line
#     # only relevant starting positions are in the top left corner
#     # k distance from the right side, and the bottom
#     possible_lines = []
#     for i in range(len(past_moves)):
#         line_rd = d_line_ld(past_moves[i], k)
#         zero_mask = np.full((arr.shape[0], arr.shape[1]), bg, dtype=int)
#         for coord in line_rd:
#             # print(coord[0], coord[1])
#             zero_mask[(coord[0], coord[1])] = line_var
#         possible_lines.append(zero_mask)
#     return possible_lines

# def has_won(game_board, list_of_lines, list_of_inverse_lines_w_player_number, player_number):
#     for i in range(len(list_of_lines)):
#         # print(game_board)
#         comparison_step_1 = list_of_lines[i] * game_board
#         # print(comparison_step_1)
#         comparison_step_2 = comparison_step_1 + list_of_inverse_lines_w_player_number[i]
#         # print(comparison_step_2)
#         all_same = np.all(comparison_step_2==player_number)
#         return all_same
    

# m, n ,k = (6, 5, 4)
# var = 1

# possible_lines_rd = place_line_rd(array, m, n, k, var, 0, line_var=1)
# inverse_possible_lines_w_player_number_rd = place_line_rd(array, m, n, k, var, var, line_var=0)



# possible_lines_ld = place_line_ld(array, m, n, k, var, 0, line_var=1)
# inverse_possible_lines_w_player_number_ld = place_line_ld(array, m, n, k, var, var, line_var=0)



# print(array)
# right_diagonal = has_won(array, possible_lines_rd, inverse_possible_lines_w_player_number_rd, player_number=var)
# left_diagonal = has_won(array, possible_lines_ld, inverse_possible_lines_w_player_number_ld, player_number=var)

# print(f"player {var} won with left diagonal: {left_diagonal}")
# print(f"player {var} won with right diagonal: {right_diagonal}")

import pandas as pd

# Given statistical data as dictionaries
data_1 = {
    "count": 383.0, "mean": 5.062663, "std": 1.153751,
    "min": 4.0, "25%": 4.0, "50%": 5.0, "75%": 5.0,
    "max": 10.0, "mode": 5.0, "range": 6.0, "variance": 1.331142,
    "skewness": 1.491248, "kurtosis": 2.492868
}
data_2 = {
    "count": 136.0, "mean": 4.713235, "std": 0.824694,
    "min": 4.0, "25%": 4.0, "50%": 5.0, "75%": 5.0,
    "max": 8.0, "mode": 4.0, "range": 4.0, "variance": 0.680120,
    "skewness": 1.141936, "kurtosis": 1.326892
}

# Converting data into Series with 'Statistics' as index
stats_1 = pd.Series(data_1)
stats_2 = pd.Series(data_2)

print(type(stats_1))

# Constructing DataFrame
df = pd.DataFrame({
    'Statistics': stats_1.index,
    'bot 1': stats_1.values,
    'bot 2': stats_2.values
})

# Displaying the DataFrame
print(df)