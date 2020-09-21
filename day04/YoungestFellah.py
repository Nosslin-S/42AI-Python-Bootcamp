from FileLoader import FileLoader

import pandas as pd


def youngestFellah(df, year):
    df_year = data[data["Year"] == year].copy()
    df_year.sort_values("Age", inplace=True)
    woman = df_year[df_year["Sex"] == "F"].reset_index().iloc[0]["Age"]
    man = df_year[df_year["Sex"] == "M"].reset_index().iloc[0]["Age"]
    return {"F": woman, "M": man}


loader = FileLoader()
data = loader.load("athlete_events.csv")
print(youngestFellah(data, 2004))
