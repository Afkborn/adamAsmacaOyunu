from os import getcwd, path
from Python.Value import Value
import pandas as pd
class Hangman:
    values = [] 
    databaseLoc = getcwd() +  fr'\Database\database.csv'

    isLoadDatabase = False
    def __init__(self,pcName,diff):
        self.pcName = pcName
        self.diff = diff
        self.loadDatabase()

    def changeDatabaseLocation(self,databaseLoc):
        if path.exists(databaseLoc):
            self.databaseLoc = databaseLoc
        else:
            print('File not exists')
    def loadDatabase(self):
        if path.exists(self.databaseLoc):
            csv_reader = pd.read_csv(self.databaseLoc, delimiter=',')
            for value,category,diffLevel in csv_reader.values:
                myObj = Value(value,category,diffLevel)
                self.values.append(myObj)
            
        else:
            print('File not exists')
