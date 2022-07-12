import pandas as pd
from FileLoader import FileLoader


# https://www.skytowner.com/explore/getting_minimum_value_in_columns_in_pandas_dataframe
# https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/
def youngestfellah(df, year):
    m = df.loc[(df['Sex'] == 'M') & (df['Year'] == year), ['Age']].min()
    f = df.loc[(df['Sex'] == 'F') & (df['Year'] == year), ['Age']].min()
    return ({'f': f.Age, 'm': m.Age})


loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(youngestfellah(data, 1992))
# output is: "{'f': 12.0, 'm': 11.0}"

print(youngestfellah(data, 2004))
# output is: "{'f': 13.0, 'm': 14.0}"

print(youngestfellah(data, 2010))
# output is: "{'f': 15.0, 'm': 15.0}"

print(youngestfellah(data, 2003))
# output is: "{'f': nan, 'm': nan}"
