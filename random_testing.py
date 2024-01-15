import numpy as np
from datetime import datetime

def mnk_board(m, n, k):
    board = np.zeros((m, n), dtype=int)
    return board

print(mnk_board(5, 6, 4))

now = datetime.now()

# Format the date and time
formatted_date = now.strftime("%y%m%d_%H-%M-%S")

print(formatted_date)