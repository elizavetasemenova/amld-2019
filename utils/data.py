import pandas as pd

class DataSet():
    def __init__(self, name="train", path="dataset"):
        self.path = path

        print("Reading dataset in %s/" %path)
        bodies = name+"_bodies.csv"
        stances = name+"_stances.csv"

        print("Loading files %s, %s" %(bodies,stances))
        self.data = self.read(bodies,stances)

    def read(self,bodies,stances):
        train_bodies = pd.read_csv(self.path + "/" + bodies)
        train_stances = pd.read_csv(self.path + "/" + stances)
        merged = train_bodies.merge(train_stances,left_on='Body ID',right_on='Body ID',how='outer')
        return merged

    def print(self):
        print(self.data.head())
