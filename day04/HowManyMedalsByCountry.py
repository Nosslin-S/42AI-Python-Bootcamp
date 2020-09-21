import pandas as pd
from FileLoader import FileLoader


def HowManyMedalsByCountry(df, country):
    my_dict = {}
    df = df[df["Team"] == country][["Year", "Medal", "Event"]]
    for year in df["Year"].drop_duplicates().sort_values():
        my_dict[year] = {
            "G": df[["Medal", "Event"]][(df["Year"] == year) & (df["Medal"] == "Gold")]
            .drop_duplicates(subset="Event")["Medal"]
            .count(),
            "S": df[["Medal", "Event"]][
                (df["Year"] == year) & (df["Medal"] == "Silver")
            ]
            .drop_duplicates(subset="Event")["Medal"]
            .count(),
            "B": df[["Medal", "Event"]][
                (df["Year"] == year) & (df["Medal"] == "Bronze")
            ]
            .drop_duplicates(subset="Event")["Medal"]
            .count(),
        }

    return my_dict
