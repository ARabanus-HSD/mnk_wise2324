import numpy as np

array = np.array([[0, 1, 0, 0, 0],
                  [0, 2, 0, 0, 0],
                  [0, 0, 2, 1, 0],
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