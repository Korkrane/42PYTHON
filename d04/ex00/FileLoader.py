import pandas as pd


class FileLoader:
    def __init__(self):
        pass

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensons", df.shape[0], "x", df.shape[1])
            return df
        except Exception as e:
            print("Error:", e)
            return None

    def display(self, df, n):
        try:
            if n == 0:
                return
            elif n > 0:
                print(df.head(n))
            else:
                print(df.tail(abs(n)))
        except Exception as e:
            print('Error', e)


loader = FileLoader()
data = loader.load("../athlete_events.csv")
loader.display(data, "lol")
loader.display(data, 12)
loader.display(data, -3)
