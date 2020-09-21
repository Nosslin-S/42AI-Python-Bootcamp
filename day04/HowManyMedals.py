import pandas as pd
from FileLoader import FileLoader


def HowManyMedals(data, name):
    my_dict = {}
    df = data[data["Name"] == name][["Year", "Medal"]].copy()
    for year in df["Year"]:
        my_dict[year] = {
            "G": df["Medal"][(df["Year"] == year) & (df["Medal"] == "Gold")].count(),
            "S": df["Medal"][(df["Year"] == year) & (df["Medal"] == "Silver")].count(),
            "B": df["Medal"][(df["Year"] == year) & (df["Medal"] == "Bronze")].count(),
        }
    return my_dict


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("athlete_events.csv")
    print(HowManyMedals(data, "Kjetil Andr Aamodt"))

