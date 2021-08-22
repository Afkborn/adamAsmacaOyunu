from re import T
import pyfiglet
import msvcrt
from keyboard import is_pressed
from os import system,environ


from Python.Hangman import Hangman

menuSecenekler = ["Start Game","Change Difficulty","About Us","Exit"]
categories = ["Countries","Cities","Animals","Plants","Random"]
diffLevelList = ['Easy','Medium','Hard']
aboutUsText = """grubumuz hakkındaki mesaj"""
okBaslangic = 0
printOneTimeMenu = True
whileControl = True
pcName = environ['COMPUTERNAME']



if __name__ == "__main__":
    diffLevel = 1
    while whileControl:
        if printOneTimeMenu:
            system('cls')
            print(pyfiglet.figlet_format('Bluecoder'))
            for index,i in enumerate(menuSecenekler):
                if index == okBaslangic:
                    print(f"\t\t> {i}")
                else:
                    print(f"\t\t{i}")
            
        printOneTimeMenu = False
        secim = msvcrt.getch()
        if secim == b"H":
            if okBaslangic == 0:
                okBaslangic == len(menuSecenekler)-1
            else:
                okBaslangic-=1
            printOneTimeMenu = True
        elif secim == b"P":
            if okBaslangic == len(menuSecenekler)-1:
                okBaslangic == 0
            else:
                okBaslangic+=1
            printOneTimeMenu = True
        elif secim == b'\x03':
            exit()
        elif secim == b'\r':
            if okBaslangic ==0:
                hangman = Hangman(pcName,diffLevel)
                hangman.loadDatabase()
                printOneTimeMenu=False
            elif okBaslangic ==1:
                printOneTimeMenu=False
                print(f"Current Difficulty: {diffLevelList[diffLevel]}")
                for index,i in enumerate(diffLevelList,start=1):
                    print(f"{index}) {i} ",end="")
                try:
                    diffLevel = int(input('\nDiff Level: '))-1
                    print(f"New Difficulty: {diffLevelList[diffLevel]}")
                    print("Press any key to continue.")
                    msvcrt.getch()
                    printOneTimeMenu=True
                except ValueError:
                    print('Check value')
                finally:
                    inputDiff = 1
                
            elif okBaslangic ==2:
                print(aboutUsText)
                printOneTimeMenu=False
            elif okBaslangic ==3:
                whileControl = False


