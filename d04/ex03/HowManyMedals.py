import pandas as pd
from FileLoader import FileLoader


def how_many_medals(df, participant):

    dfParticipant = df.loc[(df['Name'] == participant)]
    dicta = dfParticipant.to_dict()
    years = dicta['Year'].values()
    medals = dicta['Medal'].values()
    recap = {}
    for year, medal in zip(years, medals):
        if year not in recap:
            recap[year] = {'G': 0, 'S': 0, 'B': 0}
        if medal == 'Gold':
            recap[year]['G'] += 1
        elif medal == 'Silver':
            recap[year]['S'] += 1
        elif medal == 'Bronze':
            recap[year]['B'] += 1
    return recap



loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(how_many_medals(data, 'Gary Abraham'))
#  the output is: "{1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}"

print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
#  the output is "{2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}"

print(how_many_medals(data, 'Kristin Otto'))
#  the output is: "{1988: {'G': 6, 'S': 0, 'B': 0}}"
