# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

df = pd.read_csv("../data/match_data_2025.csv")

df

# %%

filtro_lta = (df["datacompleteness"] == "complete") & (df["league"] == "LTA S")

df_lta = df[filtro_lta].copy()
# %%
 
df_lta["truegamelength"] = [timedelta(seconds=i) for i in df_lta["gamelength"]] 
# %%

def f_timedelta(data):
    total_seconds = int(data.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{minutes:02}"

# %%

df_lta["truegamelength"] = df_lta["truegamelength"].apply(f_timedelta)

df_lta["truegamelength"]

# %%

df_teams = df_lta[df_lta["position"] == "team"]

df_teams
# %%
df_teams = df_teams[df_teams["split"] == "Split 3"]
# %%

df_teams
# %%

df_graphic = df_teams.groupby("teamname").agg({
    "gamelength":"mean",
    "goldat10":"mean",
    "goldat15":"mean",
    "goldat20":"mean",
    "goldat25":"mean"
}).round(2)

# %%

df_graphic["truegamelength"] = [timedelta(seconds=i) for i in df_graphic["gamelength"]]
# %%

df_graphic["truegamelength"] = df_graphic["truegamelength"].apply(f_timedelta)


# %%
df_graphic
# %%
