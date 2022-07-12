import pandas as pd
from FileLoader import FileLoader


def proportion_by_sport(df, year, sport, gender):

    # # if it was correctly made
    # beforeSportFilter = df.loc[(df['Sex'] == gender) & (df['Year'] == year)]
    # beforeSportFilterWoDuplicates = beforeSportFilter.drop_duplicates(subset=['Name'])
    # SportFilterWoDuplicates = beforeSportFilterWoDuplicates.loc[(df['Sport'] == sport)]
    # return (SportFilterWoDuplicates.shape[0] / beforeSportFilterWoDuplicates.shape[0])

    beforeSportFilter = df.loc[(df['Sex'] == gender) & (df['Year'] == year)]
    SportFilter = beforeSportFilter.loc[(df['Sport'] == sport)]
    return (SportFilter.shape[0] / beforeSportFilter.shape[0])



loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(proportion_by_sport(data, 2004, 'Tennis', 'F'), end="\n\n")

print(proportion_by_sport(data, 2008, 'Hockey', 'F'), end="\n\n")

print(proportion_by_sport(data, 1964, 'Biathlon', 'M'), end="\n\n")
