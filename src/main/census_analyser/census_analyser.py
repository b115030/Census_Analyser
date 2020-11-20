import pandas as pd


class read_from_csv:
    def __init__(self, path):
        self.path = path

    def lines_count(self):
        census_list = pd.read_csv(self.path).values.tolist()
        return len(census_list)