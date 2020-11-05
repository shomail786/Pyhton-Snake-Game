import os, time, os.path, re, sys
from difflib import SequenceMatcher
from datetime import datetime

#Opens english words file and stores into a list. 
dictList = []
with open("englishwords.txt", 'r') as file:
    for line in file:
        dictList.append(line.strip("\n"))

#Function to take in sentence input and pass into spellcheck function.
def sentenceCheck():
    while True:
        checkSentence = input("\nPlease enter the sentence you wish to check : ")
        if checkSentence != "":
            sentenceList = checkSentence.split(" ")
            spellChecker(sentenceList)
            break
        else:
            print("Invalid input, cannot be left blank")

#Main Function for spell checking.   
def spellChecker(words):
    
    #Initialises variables to store summary statistics, and takes in date and time, correctly formatting them.
    totalWords = len(words)
    correctWords = 0
    incorrectWords = 0
    addedWords = 0
    changedWords = 0
    timeDate = datetime.now()
    dateString = timeDate.strftime("%d/%m/%Y %H:%M:%S")
    start = time.time()
    
    #Variable to store original string.
    originalInput = ""
    
    #loops through sentence/file passed into the function. Removes any characters that are non alpha, and ensures all are lowercase.
    for i in words:
        i = re.sub(r'[^a-zA-Z]+', '', i.lower())
        print("\n" + i)
        
        if i in dictList:
            print("Word found")
            correctWords += 1
            originalInput = originalInput + " " + i
        
        #If word is not in dictionary, 4 options presented. Each option increments its respective summary statistic(s). Also updates original Input variable to output full string afterwards. 
        else:
            while True:
                incorrectChoice = input("Incorrect spelling - Would you like to: \nIgnore (1): \nMark as incorrect (2): \nAdd to dictionary (3): \nSuggest a correct spelling (4): ")
                if incorrectChoice == "1":
                    print("\nWord ignored")
                    incorrectWords += 1
                    originalInput = originalInput + " " + i
                    break
                
                elif incorrectChoice == "2":
                    i = "?" + i + "?"
                    print(i)
                    incorrectWords += 1
                    originalInput = originalInput + " " + i
                    break
                
                elif incorrectChoice == "3":
                    dictList.append(i)
                    with open("englishwords.txt", 'a') as file:
                        file.write("\n" + i)
                        print("Word added to dictionary!")
                        correctWords += 1
                        addedWords += 1
                        originalInput = originalInput + " " + i
                    break
                
                #Uses sequence matcher function to establish closest word to user input.
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
                        suggChoice = input("\nWould you like to : \nAccept the suggestion (1): \nReject the suggestion (2): ")
                        if suggChoice == "1":
                            i = suggWord
                            print("\nSuggestion accepted")
                            correctWords += 1
                            changedWords += 1
                            originalInput = originalInput + " " + i
                            break
                        
                        elif suggChoice == "2":
                            print("\nSuggestion rejected")
                            incorrectWords += 1
                            originalInput = originalInput + " " + i
                            break
                        
                        else:
                            print("\nInvalid input. Please only enter either 1 or 2.")
                    break
                else:
                    print("\nIncorrect input. Please type either 1, 2, 3 or 4.")
    
    #Calculates the total time elapsed.
    end = time.time()
    timeElapsed = end - start
    
    #Concatenates all summary statistics and saves them into user specified file. 
    summary = ("\nSummary Statistics : \nTotal Words : " + str(totalWords) + "\nNumber of Correct Words : " + str(correctWords) + "\nNumber of Incorrect Words : " + str(incorrectWords) + "\nNumber of Added Words : " + str(addedWords) + "\nNumber of Changed Words : " + str(changedWords) + "\nDate and Time of Spellcheck : " + str(dateString) + "\nTime Elapsed : " + str(timeElapsed) + " Seconds " "\nInput : " + originalInput)
    print(summary)
    statsFileName = input("\nPlease enter a filename for the spellcheck file : ")
    statsFile = open(statsFileName, "w")
    statsFile.write(summary)
    statsFile.close
    print("\nFile Saved")
    while True:
        option = input("\nWould you like to return to the main menu (1) or Quit (2) : ")
        if option == "1":
            break
        elif option == "2":
            print("Exiting program ... ")
            time.sleep(2)
            sys.exit()

#Main menu - Validated input, only allows for input of 1, 2 or 0.
while True:
    menuChoice = input("\nMain Menu:\nPlease Select An Option : \nEnter a sentence (1) : \nEnter a file name (2) : \nExit (0) : ")
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