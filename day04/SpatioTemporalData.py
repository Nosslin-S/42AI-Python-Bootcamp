import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def where(self, year):
        return list(data[data["Year"] == year]["City"].drop_duplicates(keep="first"))

    def when(self, location):
        return list(
            data[data["City"] == location]["Year"].drop_duplicates(keep="first")
        )


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("athlete_events.csv")
    dater = SpatioTemporalData()
    print(dater.where(2016))
    print(dater.when("Paris"))
