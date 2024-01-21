""" 
# Main Game Log:
adds entry to dp (.csv) looking like this
| player1_type | player2_type | starting_player | winning_player |
|--------------|--------------|-----------------|----------------|
| player       | player       | 1               | 0              |
| bot_random   | bot_random   | 2               | 1              |
| bot_simple   | bot_simple   | 1               | 2              |
| bot_complex  | bot_complex  | 2               | 0              |
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game_log.csv")
df_svs = pd.read_csv("game_log_simple_vs_simple.csv")

print(df)

def sort_winners(df):
    win_counter_bot_random = 0
    win_counter_bot_simple = 0
    draw_count = 0

    for index, row in df.iterrows():
        if row['player1_type'] == "bot_simple" and row['winning_player'] == 1:
            win_counter_bot_simple += 1
        elif row['player2_type'] == "bot_simple" and row['winning_player'] == 2:
            win_counter_bot_simple += 1
        if row['player1_type'] == "bot_random" and row['winning_player'] == 1:
            win_counter_bot_random += 1
        elif row['player2_type'] == "bot_random" and row['winning_player'] == 2:
            win_counter_bot_random += 1
        if row["winning_player"] == 0:
            draw_count += 1

        counter_dict = [{"bot_random": win_counter_bot_random, "bot_simple": win_counter_bot_simple, "draw": draw_count}]
        df_counter = pd.DataFrame.from_dict(counter_dict)
    return df_counter

def sort_winners_svs(df):
    win_counter_bot_simple_1 = 0
    win_counter_bot_simple_2 = 0
    draw_count = 0

    for index, row in df.iterrows():
        if row['player1_type'] == "bot_simple" and row['winning_player'] == 1:
                win_counter_bot_simple_1 += 1
        elif row['player2_type'] == "bot_simple" and row['winning_player'] == 2:
                win_counter_bot_simple_2 += 1
        if row["winning_player"] == 0:
            draw_count += 1
        
        counter_dict = [{"starting_simple": win_counter_bot_simple_1, "second_simple": win_counter_bot_simple_2, "draw": draw_count}]
        df_counter = pd.DataFrame.from_dict(counter_dict)
    return df_counter

sorted_dataframe = sort_winners_svs(df_svs)
print(sorted_dataframe)
sorted_dataframe.plot(kind='bar')
plt.title('W/L/D rate of games')
plt.xlabel('Bot Types')
plt.ylabel('Games')
plt.show()