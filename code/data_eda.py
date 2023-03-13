import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data_loc = "../data_files/"

# Start with NBA Data 

lines_df, spread_df = pd.read_csv(data_loc+'nba_hist_data/nba_betting_money_line.csv'),\
    pd.read_csv(data_loc+'nba_hist_data/nba_betting_spread.csv')
total_df, games_df = pd.read_csv(data_loc+'nba_hist_data/nba_betting_totals.csv'),\
    pd.read_csv(data_loc+'nba_hist_data/nba_games_all.csv')
# players_df, player_game_df = pd.read_csv(data_loc+'nba_hist_data/nba_players_all.csv'),\
#     pd.read_csv(data_loc+'nba_hist_data/nba_players_game_stats.csv')
# teams_df = pd.read_csv(data_loc+'nba_hist_data/nba_teams_all.csv')

comb_spread = lines_df.merge(
    spread_df,
    how='inner',
    on=['game_id', 'book_id'],
    suffixes=('_ml', '_spread')
)


print(len(lines_df))
print(len(comb_spread))
print(len(spread_df))

print(comb_spread.isnull().sum())
# print(spread_df.head())
# print('\n')
# print(spread_df.columns)