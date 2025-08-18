# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/match_data_2025.csv")

df

# %%

filtro_lta = (df["datacompleteness"] == "complete") & (df["league"] == "LTA S")

df = df[filtro_lta]

df

# %%

def timedelta(coluna):
    for i in df[coluna]:


# %%

