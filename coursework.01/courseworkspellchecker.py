import os, time, os.path
from difflib import SequenceMatcher
from datetime import datetime
dictList = []
with open("englishwords.txt", 'r') as file:
    for line in file:
        dictList.append(line.strip("\n"))
    
def sentenceCheck():
    checkSentence = input("\nPlease enter the sentence you wish to check : ")
    sentenceList = checkSentence.split(" ")
    print(sentenceList)
    spellChecker(sentenceList)

    
def spellChecker(words):
    totalWords = len(words)
    correctWords = 0
    incorrectWords = 0
    addedWords = 0
    changedWords = 0
    timeDate = datetime.now()
    dateString = timeDate.strftime("%d/%m/%Y %H:%M:%S")
    start = time.time()
    


    for i in words:
        print("\n" + i)
        if i in dictList:
            print("Word found")
            correctWords += 1
        else:
            while True:
                incorrectChoice = input("\nIncorrect spelling - Would you like to: \nIgnore (1): \nMark as incorrect (2): \nAdd to dictionary (3): \nSuggest a correct spelling (4): ")
                if incorrectChoice == "1":
                    print("\nWord ignored")
                    incorrectWords += 1
                    break
                
                elif incorrectChoice == "2":
                    i = "?" + i + "?"
                    print(i)
                    incorrectWords += 1
                    break
                elif incorrectChoice == "3":
                    dictList.append(i)
                    with open("englishwords.txt", 'a') as file:
                        file.write("\n" + i)
                        print("Word added to dictionary!")
                    break
                elif incorrectChoice == "4":
                    score = 0
                    suggWord = ""
                    for word in dictList:
                        newScore = SequenceMatcher(None, word, i).ratio()
                        if newScore > score:
                            score = newScore
                            suggWord = word
                    print("Suggested word is " + suggWord)
                    while True:
                        suggChoice = input("\nWOuld you like to : \nAccept the suggestion (1): \nReject the suggestion (2): ")
                        if suggChoice == "1":
                            print("\nSuggestion accepted")
                            break
                        elif suggChoice == "2":
                            print("\nSuggestion rejected")
                            break
                        else:
                            print("\nInvalid input. Please only enter either 1 or 2.")
                    break
                else:
                    print("\nIncorrect input. Please type either 1, 2, 3 or 4.")
    end = time.time()
    timeElapsed = end - start
    print(timeElapsed)

while True:
    menuChoice = input("\nMain Menu:\nPlease type (1) to enter a word, (2) to enter a file name, or (0) to exit : ")
    if menuChoice in ["1", "2", "0"]:
        if menuChoice == "1":
            sentenceCheck()
                

        elif menuChoice == "2":
            valChoice = False
            while valChoice == False:
                fNameCheck = input("\nPlease enter the filename that you would like to check, along with the .txt extension : ")
                try:
                    with open(fNameCheck, 'r') as file:
                        
                        fileList = file.read()
                        fileWords = fileList.split(" ")
                        print(fileWords)
                        spellChecker(fileWords)
                        valChoice = True
                except FileNotFoundError:
                    print("\nFile does not exist.")
                    valInput = False
                    while valInput == False:
                        choice = input("\nWould you like to :\n\nRe-enter the filename (1)\n\nReturn to main menu (2) ")
                        if choice == "1":
                            valInput = True
                        elif choice == "2":
                            valInput = True
                            valChoice = True
                        else:
                            print("\nInvalid input\nPlease enter either 1 or 2.")   

        elif menuChoice == "0":
            print("Exiting program ... ")
            time.sleep(2)
            break
        
    else:
        print("\nPlease only enter either 1, 2 or 3")