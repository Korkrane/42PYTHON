import pandas as pd
from FileLoader import FileLoader


def how_many_medals(df, participant):

    # # if it was correctly made
    # beforeSportFilter = df.loc[(df['Sex'] == gender) & (df['Year'] == year)]
    # beforeSportFilterWoDuplicates = beforeSportFilter.drop_duplicates(subset=['Name'])
    # SportFilterWoDuplicates = beforeSportFilterWoDuplicates.loc[(df['Sport'] == sport)]
    # return (SportFilterWoDuplicates.shape[0] / beforeSportFilterWoDuplicates.shape[0])

    dfParticipant = df.loc[(df['Name'] == participant)]
    print(dfParticipant)
    return {}


loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(how_many_medals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(how_many_medals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
