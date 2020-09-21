import pandas as pd
from FileLoader import FileLoader


def ProportionBySport(df, year, sport, gender):
    filtered_df = (
        data[(data["Year"] == year) & (data["Sex"] == gender)]
        .copy()
        .drop_duplicates(subset="Name", keep="first")
    )
    filtered_df["Participant"] = 1
    grouped_df = filtered_df.groupby("Sport").sum()
    return grouped_df.loc[sport]["Participant"] / sum(grouped_df["Participant"])


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("athlete_events.csv")
    print(ProportionBySport(data, 2004, "Tennis", "F"))

