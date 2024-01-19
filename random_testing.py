import numpy as np

array = ([0, 1, 0, 3, 0],
         [0, 0, 3, 0, 0],
         [0, 3, 0, 1, 0],
         [3, 0, 1, 0, 1],
         [0, 1, 0, 0, 0],
         [1, 2, 2, 0, 0])


def find_var(arr, var):
    past_moves = np.argwhere(arr == var)
    print(past_moves)
    pass
    # return list_of_ones # list of all ones on the board, prepared for np.take

search_position = 3 # first player number on board
placement_list = []
# find first player number
    # extreact index (?) 
for i in range(4): # replace with winning length
    x = np.take(array, i+ search_position)
    # search_position += 3 # self.board.m -2 num cols on board /
    search_position += 5 # self.board.m num cols on board \
    placement_list.append(x)
print(placement_list)


all_same = all(x==placement_list[0] for x in placement_list)
print(all_same)

# for i in range(len(placement_list)):
#     if placement_list[i] == 3:
#         print("all moves are same!")

find_var(array, 3)
print(np.where(array==1)[0])