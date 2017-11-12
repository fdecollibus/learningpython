# While Loops
import os

def printHangMan(livesLeft,livesMax):
    vitality = livesLeft / livesMax
    if vitality < 1.0:
        print (" _________    ")
    if vitality < 0.8:
        print ("|        |    ")
    if vitality < 0.6:
        print ("|        0    ")
    if vitality < 0.4:
        print ("|       /|\\  ")
    if vitality < 0.2:
        print ("|       / \\  ")
    if vitality < 0.1:
        print ("|       | |     ")
        print ("|             ")


def stillInGame(livesLeft):
    if livesLeft > 0:
        return True
    else:
        return False

def didIWin(currGuessed, maxGuessed):
    if (currGuessed == maxGuessed):
        return True
    else:
        return False

def captureContinueGame():
    inputNotCorrect = True
    while inputNotCorrect:
        decision = input("Do you want to continue playing? ")
        print(decision.lower())
        if ((decision[0].lower()=="y") or (decision[0].lower()=="n")):
            inputNotCorrect = False
    if (decision[0].lower()=="y"):
        return True
    else: return False

keepPlaying = True
while (keepPlaying):
    os.system('clear')
    stringToGuess= input("Insert your String to guess:? ")
    livesMax = int(input("Insert max number of guesses:? "))
    input("let's start!- Press a key")
    os.system('clear')
    livesLeft = livesMax
    enigma = list(stringToGuess)
    enigmaLowerCase =list(stringToGuess.lower())
    currentlyGuessed = 0
    enigmaToGuess = list(len(enigmaLowerCase)*("_"))
    enigmaSetContains= set(enigmaLowerCase)
    enigmaCountToGuess= len(enigmaSetContains)
    inGame = True
    while ((inGame) and (not (didIWin(currentlyGuessed, enigmaCountToGuess)))):
        print("You have {} of maximum attempts {} left".format(livesMax,livesLeft))
        printHangMan(livesLeft,livesMax)
        print(enigmaToGuess)
        guess = input("insert you guess:? ").lower()
        if (guess[0] in enigmaSetContains):
            print("Guess found!")
            for i in range(len(enigmaLowerCase)):
                if (enigmaLowerCase[i]==guess[0]):
                    enigmaToGuess[i]=enigma[i]
                    ''' Against duplicates letters found '''
                    if guess[0] in enigmaSetContains:
                        enigmaSetContains.remove(guess[0])
                        currentlyGuessed+=1
        else: livesLeft-=1
        inGame=stillInGame(livesLeft)
        if (not inGame) :
            print("Sorry, game over")
            printHangMan(livesLeft,livesMax)
    if (didIWin(currentlyGuessed, enigmaCountToGuess)):
        print("Congratulation, you won!")
    keepPlaying = captureContinueGame()
