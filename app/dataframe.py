import pandas as pd

stats = pd.read_csv('nfl_stats_2014.csv')


stats = stats.drop('pass_comp',1).drop('')