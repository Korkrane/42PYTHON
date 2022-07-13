import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        t = self.df.loc[(self.df['City'] == location)]
        e = t['Year'].drop_duplicates()
        years = []
        for i in e:
            years.append(i)
        return years

    def where(self, date):
        t = self.df.loc[(self.df['Year'] == date)]
        e = t['City'].drop_duplicates()
        cities = []
        for i in e:
            cities.append(i)
        return cities


loader = FileLoader()
data = loader.load("../athlete_events.csv")

sp = SpatioTemporalData(data)

print(sp.where(2000))
# output is: ['Sydney']

print(sp.where(1980))
# output is: ['Lake Placid', 'Moskva'] If a single of these locations is returned it's ok.

print(sp.when('London'))
# output is: [2012, 1948, 1908]