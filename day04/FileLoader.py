import pandas as pd
import numpy as np


class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}")
        return data

    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("athlete_events.csv")
    loader.display(data, -8)

