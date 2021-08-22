from random import randint
from os import getcwd, path

from Python.Value import Value
import pandas as pd


class Hangman:
    __values = [] 
    databaseLoc = getcwd() +  fr'\Database\database.csv'
    __chosenWord = "None"
    __isLoadDatabase = False
    __selectedWords = []


    def __init__(self,pcName,diff = 1):
        self.pcName = pcName
        self.diff = diff
        self.__loadDatabase()

    def changeDatabaseLocation(self,databaseLoc):
        if path.exists(databaseLoc):
            self.databaseLoc = databaseLoc
            self.__loadDatabase()
        else:
            print('File not exists')

    def changeDiff(self,diff):
        self.diff = diff

    def getDiff(self):
        return self.diff

    def __loadDatabase(self):
        if path.exists(self.databaseLoc):
            csv_reader = pd.read_csv(self.databaseLoc, delimiter=',')
            for value,category,diffLevel in csv_reader.values:
                myObj = Value(value,category,diffLevel)
                self.__values.append(myObj)
            self.__isLoadDatabase = True
        else:
            print('File not exists')
    
    def __chooseWord(self):
        control = True
        while control:
            if len(self.__selectedWords) == len(self.__values):
                self.__selectedWords.clear()
            randomValue = self.__getRandomValue()
            selectedValue = self.__values[randomValue].getValue()
            if selectedValue in self.__selectedWords:
                control = True
            else:
                control = False
                self.__chosenWord = selectedValue
                self.__selectedWords.append(self.__chosenWord)


    def __getRandomValue(self)->int:
        return randint(0,len(self.__values)-1)

    def startGame(self):
        if self.__isLoadDatabase:
            self.__chooseWord()

        else:
            print("Error (database error)")
        
