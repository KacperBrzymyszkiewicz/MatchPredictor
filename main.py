import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from narwhals import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
team_name = "Man City"
df = pd.read_csv("./dane.csv")
print(df)
def all_matches(team_name):
    teamstats = df[(df["HomeTeam"] == team_name) | (df["AwayTeam"] == team_name)].copy()
    teamstats["Goals"] = np.where(
        teamstats["HomeTeam"] == team_name,
        teamstats["FTHG"],
        teamstats["FTAG"]
    )
    teamstats["MatchNumber"] = range(1,len(teamstats)+1)
    return teamstats


teamstats = all_matches(team_name)
a,b = np.polyfit( teamstats["MatchNumber"],teamstats["Goals"], 1)
trend = a * teamstats["MatchNumber"] + b
# print(a,b)
# print(teamstats[["Goals","MatchNumber"]])
plt.figure(figsize=(len(teamstats),5))
plt.plot(teamstats["MatchNumber"], trend, color="red")
plt.scatter(teamstats["MatchNumber"],teamstats["Goals"])
plt.xlabel(team_name)
plt.ylabel("Goals")
plt.show()