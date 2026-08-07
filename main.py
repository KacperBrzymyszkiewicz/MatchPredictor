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
data = sd.FBref(
    leagues="POL-Ekstraklasa",
    seasons="2025",
    data_dir=Path(r"C:\ProjektyPython\Projekt\Cache")
)
stats = data.read_schedule()
print(stats.columns.tolist())
team_stats_before = stats.loc[(stats["home_team"] == team_name) | (stats["away_team"] == team_name)].copy()
class season_team_stats:

    def __init__(self,stats,team_name):
        self.goals_scored = sum(np.where(stats["home_team"]==team_name,stats["score"].str[0].astype(int),stats["score"].str[2].astype(int)))
        self.goals_conceded = sum(np.where(stats["home_team"] != team_name, stats["score"].str[0].astype(int), stats["score"].str[2].astype(int)))

team_stats_after = season_team_stats(team_stats_before,"Lech Poznań")
print(team_stats_after)

#a,b = np.polyfit( teamstats["MatchNumber"],teamstats["Goals"], 1)
#trend = a * teamstats["MatchNumber"] + b
#print(teamstats[teamstats["Res"] == "Win"]["Goals"].sum()/(teamstats["Res"]=="Win").sum())
# print(a,b)
# print(teamstats[["Goals","MatchNumber"]])
# plt.figure(figsize=(len(teamstats),5))
# plt.plot(teamstats["MatchNumber"], trend, color="red")
# plt.scatter(teamstats["MatchNumber"],teamstats["Goals"])
# plt.xlabel(team_name)
# plt.ylabel("Goals")
# plt.show()
# plt.figure(figsize=(len(teamstats["Res"] == "Win"),teamstats["Goals"].max()+1))
# plt.scatter(teamstats[teamstats["Res"] == "Win"]["MatchNumber"],teamstats[teamstats["Res"] == "Win"]["Goals"])
# plt.xticks(teamstats[teamstats["Res"] == "Win"]["MatchNumber"])
# plt.yticks(range(0, teamstats["Goals"].max() + 1))
# plt.show()