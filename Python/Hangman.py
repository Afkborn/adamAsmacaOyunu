from random import randint
from os import getcwd, path, system
import sys
import msvcrt
import pyfiglet

from Python.Value import Value
import pandas as pd

GAMESCREEN = f"""
"""
class Hangman:

    databaseLoc = getcwd() +  fr'\Database\database.csv'
    __score = 0
    __winStat = False
    __numberOfLives = 10
    __values = [] 
    __chosenWord = "None"
    __chosenWordList = []
    __lenChosenWord = 0
    __isLoadDatabase = False
    __selectedWords = []
    __chosenWordLetters = dict()
    __enteredLetters = []
    __knownLetters = []
    __remLetterCount = 0 # kalan harf sayisi

    def __init__(self,pcName,diff = 1):
        self.__pcName = pcName
        self.__diff = diff
        self.__loadDatabase()

    def changeDatabaseLocation(self,databaseLoc):
        if path.exists(databaseLoc):
            self.databaseLoc = databaseLoc
            self.__loadDatabase()
        else:
            print('File not exists')

    def changeDiff(self,diff):
        self.__diff = diff

    def getDiff(self):
        return self.__diff

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
                    if not i in self.__chosenWordList:
                        self.__chosenWordList.append(i)
                    iValue = self.__chosenWordLetters.get(i,-1)
                    if iValue == -1:
                        self.__chosenWordLetters[i] = 1
                    else:
                        self.__chosenWordLetters[i] += 1
                self.__lenChosenWord = len(selectedValue)
                self.__remLetterCount = self.__lenChosenWord
                self.__selectedWords.append(self.__chosenWord)
        print(self.__chosenWordLetters)
        print(self.__chosenWord)



    def __getRandomValue(self)->int:
        return randint(0,len(self.__values)-1)

    def __printGameScreen(self):


        print(f"\n\n\nBURAYA ADAM ASMANIN AKTİF DURUMUNU BELİRTEN GRAFİK ÇİZİLECEK Şimdilik can yazsın: {self.__numberOfLives}\n\n\n")
        print("\t\t\t",end=" ")
        for i in self.__chosenWord:
            if i in self.__knownLetters:
                print(i,end=" ")
            else:
                print("_",end=" ")

        print(f"\nEntered Letters: {','.join(self.__enteredLetters)}\n")

    def __printWinScreen(self):
        self.__calculateScore()
        print(pyfiglet.figlet_format(f'WIN'))
        print(f"SCORE: {self.__score}")
        print("press any key to return to the main menu and  'q' for exit")
        inputText = msvcrt.getwch()
        if inputText == 'q':
            exit()
        else:
            self.__resetGame()
            self.__goMainMenu()

    def __printLoseScreen(self):
        self.__calculateScore()
        print(pyfiglet.figlet_format(f'LOSE'))
        print(f"SCORE: {self.__score}")
        print("press any key to return to the main menu and 'q' for exit")
        inputText = msvcrt.getwch()
        if inputText == 'q':
            exit()
        else:
            self.__resetGame()
            self.__goMainMenu()
    
    def __goMainMenu(self):
        pass

    def __getLetter(self):
        print(self.__chosenWordLetters)
        print(f"Kalan harf sayısı: {self.__remLetterCount}")
        letter = msvcrt.getwch()
        letter = letter.lower().strip()
        if len(letter ) == 1: #CHECK LETTER LENGHT
            
            if letter in self.__chosenWordList:
                self.__chosenWordList.remove(letter)
                lenLetter = self.__chosenWordLetters.get(letter,-1)
                print(f"Evet doğru bildin, {letter} harfinden {lenLetter} tane var.")
                if not letter in self.__enteredLetters:
                    self.__enteredLetters.append(letter)
                self.__remLetterCount -= lenLetter
                self.__knownLetters.append(letter)
            else:
                if not letter in self.__enteredLetters:
                    self.__enteredLetters.append(letter)
                self.__numberOfLives -=1
                print(f"Maalesef yanlış seçim, {self.__numberOfLives} hakkın kaldı.")
                pass


    def __checkWinStatus(self):
        if self.__remLetterCount == 0 and self.__numberOfLives >= 0:
            self.__winStat = True
            self.__printWinScreen()
            
        else:
            self.__winStat = False
            self.__printLoseScreen()
            


    def __resetGame(self):
        self.__chosenWordList = []
        self.__score = 0
        self.__winStat = False
        self.__numberOfLives = 10
        self.__lenChosenWord = 0
        self.__chosenWordLetters = dict()
        self.__enteredLetters = []
        self.__knownLetters = []
        self.__remLetterCount = 0 # kalan harf sayisi

    def __calculateScore(self):
        winLoseCont = 25 # kaybettiyse 25 puan
        if self.__winStat:
            winLoseCont = 100 # kazandıysa 100 puan

        lifeCont = self.__numberOfLives * 15 # kalan can sayısının 15 katı puan

        # Burada ise bilinen kelimede kaç tane tekrar eden harf var onu kontrol ediyoruz.
        # Örneğin adana kelimesini ele alalım. 
        # Adana da 3 tane a var bundan dolayı ilk A için 10 ikinci ve ücüncü için 5 puan alıyor.
        # Kısaca tahmin edilmesi gereken kelimede bir harf birden fazla varsa fazlalıklar için az puan alıyor.

        letterCont = 0
        for letter in self.__knownLetters:
            letterCount = self.__chosenWordLetters.get(letter,-1)
            if letterCount != -1:
                if letterCount == 1:
                    letterCont += 10
                elif letterCount > 1:
                    letterCont += (letterCont -1 * 5) + 10

        #kelime ne kadar uzunsa 5 katı kadar fazladan puan alıyor
        lenCont = self.__lenChosenWord * 5
        self.__score = winLoseCont + lifeCont + letterCont + lenCont

    def startGame(self):
        if self.__isLoadDatabase:
            self.__chooseWord()
            whileControl = True
            while whileControl:
                self.__printGameScreen()
                if self.__numberOfLives == 0:
                    whileControl = False
                    self.__checkWinStatus()
                    self.__printGameScreen()
                    
                elif self.__remLetterCount == 0:
                    whileControl = False
                    self.__checkWinStatus()
                    self.__printGameScreen()
                else:
                    
                    self.__getLetter()

        else:
            print("Error (database error)")
        
