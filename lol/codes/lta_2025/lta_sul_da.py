# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.ticker import FuncFormatter

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

def y_formatter(y, pos):
    return f'{x/1000:.0f}K' if x >= 1000 else str(x)

# %%

x = [10, 15, 20, 25]

fig, ax = plt.subplots()

for idx in df_graphic.index:

    if idx == "paiN Gaming":
        y = df_graphic.loc[idx][1:5]
        ax.plot(x, y, color='red', linewidth=1)

    elif idx == "FURIA":
        y = df_graphic.loc[idx][1:5]
        ax.plot(x, y, color='k', linewidth=1)

    else:
        y = df_graphic.loc[idx][1:5]
        ax.plot(x, y, color='gray', linewidth=0.5)

ax.yaxis.set_major_formatter(FuncFormatter(y_formatter))
ax.set_title("Ouro por tempo")
ax.set_xlabel("Minutos")
ax.set_ylabel("Ouro (K)")
ax.set_xticks([10, 15, 20, 25])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()

# %%
