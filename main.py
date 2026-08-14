import json
from os import path
from pathlib import PosixPath

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import soccerdata as sd
from narwhals import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("./POL.csv")
from pathlib import Path
#print(response)
#print(df)
team_name="Lech Poznań"


class season_team_stats:

    def __init__(self,stats,team_name):
        self.goals_scored = sum(np.where(stats["home_team"]==team_name,stats["score"].str[0].astype(int),stats["score"].str[2].astype(int)))
        self.goals_conceded = sum(np.where(stats["home_team"] != team_name, stats["score"].str[0].astype(int), stats["score"].str[2].astype(int)))

team_stats_object = season_team_stats(team_stats_before,"Lech Poznań")

print(team_stats_object.goals_scored)

def graph_goals_throughout_season(data):
    print(max(data["GF"]))
    plt.hist(data["GF"],bins=[x - 0.5 for x in range(int(max(data["GF"]+2)))],edgecolor="black")
    plt.xlabel(f"Liczba zdobytych goli {team_name}")
    plt.ylabel("Liczba meczów")
    plt.xticks(range(min(data["GF"]),max(data["GF"]+2)))
    plt.show()


#graph_goals_throughout_season(stats_match)
