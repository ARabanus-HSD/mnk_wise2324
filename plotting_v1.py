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

plt.style.use("bmh")
plt.style.use("ggplot")

df = pd.read_csv("game_log.csv")


def sort_by_match_type(df, player1, player2):
    """

    player one starts matches
    player1: string of player name
    player2: string of player name
    """
    temp_data_list = []
    for index, row in df.iterrows():
        if row["player1_type"] == player1 and row["player2_type"] == player2:
            temp_data_list.append(row)
    one_match = pd.DataFrame(temp_data_list)

    return one_match


def sort_winners(df):
    win_counter_player_1 = 0
    win_counter_player_2 = 0
    draw_count = 0

    for index, row in df.iterrows():
        if row["winning_player"] == 1:
            win_counter_player_1 += 1
        elif row["winning_player"] == 2:
            win_counter_player_2 += 1
        elif row["winning_player"] == 0:
            draw_count += 1

    counter_dict = [
        {
            "win p1": win_counter_player_1,
            "win p2": win_counter_player_2,
            "draw": draw_count,
        }
    ]

    df_counter = pd.DataFrame.from_dict(counter_dict)
    return df_counter


# splitting dataframes into matches
mcts_vs_random = sort_by_match_type(df, "bot_MCTS", "bot_random")
mcts_vs_simple_1 = sort_by_match_type(df, "bot_MCTS", "bot_simple")
mcts_vs_simple_2 = sort_by_match_type(df, "bot_MCTS", "bot_simple_2")
mcts_vs_mcts = sort_by_match_type(df, "bot_MCTS", "bot_MCTS")

simple_1_vs_random = sort_by_match_type(df, "bot_simple", "bot_random")
simple_1_vs_simple_1 = sort_by_match_type(df, "bot_simple", "bot_simple")
simple_1_vs_simple_2 = sort_by_match_type(df, "bot_simple", "bot_simple_2")
simple_1_vs_mcts = sort_by_match_type(df, "bot_simple", "bot_MCTS")

simple_2_vs_random = sort_by_match_type(df, "bot_simple_2", "bot_random")
simple_2_vs_simple_1 = sort_by_match_type(df, "bot_simple_2", "bot_simple")
simple_2_vs_simple_2 = sort_by_match_type(df, "bot_simple_2", "bot_simple_2")
simple_2_vs_mcts = sort_by_match_type(df, "bot_simple_2", "bot_MCTS")

random_vs_random = sort_by_match_type(df, "bot_random", "bot_random")
random_vs_simple_1 = sort_by_match_type(df, "bot_random", "bot_simple")
random_vs_simple_2 = sort_by_match_type(df, "bot_random", "bot_simple_2")
random_vs_mcts = sort_by_match_type(df, "bot_random", "bot_MCTS")

dfs_as_list = [
    mcts_vs_random,
    mcts_vs_simple_1,
    mcts_vs_simple_2,
    mcts_vs_mcts,
    simple_2_vs_random,
    simple_2_vs_simple_1,
    simple_2_vs_simple_2,
    simple_2_vs_mcts,
    simple_1_vs_random,
    simple_1_vs_simple_1,
    simple_1_vs_simple_2,
    simple_1_vs_mcts,
    random_vs_random,
    random_vs_simple_1,
    random_vs_simple_2,
    random_vs_mcts,
]

titles_as_list = [
    "MCTS vs Random",
    "MCTS vs Simple 1",
    "MCTS vs Simple 2",
    "MCTS vs MCTS",
    "Simple 2 vs Random",
    "Simple 2 vs Simple 1",
    "Simple 2 vs Simple 2",
    "Simple 2 vs MCTS",
    "Simple 1 vs Random",
    "Simple 1 vs Simple 1",
    "Simple 1 vs Simple 2",
    "Simple 1 vs MCTS",
    "Random vs Random",
    "Random vs Simple 1",
    "Random vs Simple 2",
    "Random vs MCTS",
]


n_rows = 4
n_cols = 4

fig, axes = plt.subplots(figsize=(15, 40), dpi=80, nrows=n_rows, ncols=n_cols)

counter = 0
for row in range(n_rows):
    for col in range(n_cols):
        sort_winners(dfs_as_list[counter]).plot(
            ax=axes[row, col], kind="bar", title=titles_as_list[counter], xticks=[]
        )
        counter += 1

plt.show()
