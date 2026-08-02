import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from narwhals import DataFrame
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
team_name = "Lech Poznan"
df = pd.read_csv("./POL.csv")

print(df)
def all_matches(team_name):
    teamstats = df.loc[(df["Season"]=="2025/2026") & ((df["Home"] == team_name) | (df["Away"] == team_name)),["Home","Away","HG","AG","Res"]].copy()
    teamstats["Goals"] = np.where(
        teamstats["Home"] == team_name,
        teamstats["HG"],
        teamstats["AG"]
    )
    teamstats["Res"] = np.select([((teamstats["Home"] == team_name) & (teamstats["Res"] == "H")),((teamstats["Away"] == team_name) & (teamstats["Res"] == "A")),(teamstats["Res"] == "D")],["Win","Win","Draw"],default="Lose")
    teamstats["MatchNumber"] = range(1,len(teamstats)+1)
    print(teamstats)
    return teamstats


teamstats = all_matches(team_name)



a,b = np.polyfit( teamstats["MatchNumber"],teamstats["Goals"], 1)
trend = a * teamstats["MatchNumber"] + b
print(teamstats[teamstats["Res"] == "Win"]["Goals"].sum()/(teamstats["Res"]=="Win").sum())
# print(a,b)
# print(teamstats[["Goals","MatchNumber"]])
# plt.figure(figsize=(len(teamstats),5))
# plt.plot(teamstats["MatchNumber"], trend, color="red")
# plt.scatter(teamstats["MatchNumber"],teamstats["Goals"])
# plt.xlabel(team_name)
# plt.ylabel("Goals")
# plt.show()
plt.figure(figsize=(len(teamstats["Res"] == "Win"),teamstats["Goals"].max()+1))
plt.scatter(teamstats[teamstats["Res"] == "Win"]["MatchNumber"],teamstats[teamstats["Res"] == "Win"]["Goals"])
plt.xticks(teamstats[teamstats["Res"] == "Win"]["MatchNumber"])
plt.yticks(range(0, teamstats["Goals"].max() + 1))

plt.show()