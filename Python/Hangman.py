from random import randint
from os import getcwd, path, system
import sys

from Python.Value import Value
import pandas as pd

GAMESCREEN = f"""
"""
class Hangman:


    __numberOfLives = 10

    __values = [] 
    databaseLoc = getcwd() +  fr'\Database\database.csv'
    __chosenWord = "None"
    __lenChosenWord = 0
    __isLoadDatabase = False
    __selectedWords = []

    __chosenWordLetters = dict()
    __enteredLetters = []
    __knownLetters = []


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
                for i in self.__chosenWord:
                    iValue = self.__chosenWordLetters.get(i,-1)
                    if iValue == -1:
                        self.__chosenWordLetters[i] = 1
                    else:
                        self.__chosenWordLetters[i] += 1
                self.__lenChosenWord = len(selectedValue)
                self.__selectedWords.append(self.__chosenWord)


    def __getRandomValue(self)->int:
        return randint(0,len(self.__values)-1)

    def __printGameScreen(self):
        #TODO oyun ekranını yazdır.
        # system('cls')
        print(f"\n\n\nBURAYA ADAM ASMANIN AKTİF DURUMUNU BELİRTEN GRAFİK ÇİZİLECEK Şimdilik can yazsın: {self.__numberOfLives}\n\n\n")
        print("\t\t\t",end=" ")
        for i in self.__chosenWord:
            if i in self.__knownLetters:
                print(i,end=" ")
            else:
                print("_",end=" ")
        print(f"\nEntered Letters: {','.join(self.__enteredLetters)}\n")



    
    def __getLetter(self):
        #TODO girilen harfin kurallara uyup uymadığını kontrol et
        letter = input("Bir harf giriniz : ")
        if letter in self.__chosenWord:
            self.__enteredLetters.append(letter)
            self.__knownLetters.append(letter)
        else:
            self.__enteredLetters.append(letter)
            self.__numberOfLives -=1
            pass


    def __checkWinStatus(self):
        #TODO kazanma kaybetme durumunu hesaplayan fonksiyonu yaz
        pass


    def __resetGame(self):
        #TODO oyunu tekrar başlatmaya hazırlayan fonksiyonu yaz
        pass


    def startGame(self):
        if self.__isLoadDatabase:
            self.__chooseWord()
            while self.__numberOfLives >= 0:
                self.__printGameScreen()
                self.__getLetter()
            
            #kazanıp kazanmama durumunu kontrol et
            

        else:
            print("Error (database error)")
        
