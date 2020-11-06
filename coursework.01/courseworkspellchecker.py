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
        print("\n\u2554"+"\u2550"*60+"\u2557")
        checkSentence = input("""
        Please enter the sentence you wish to check : 
        """ + "\n\u255A"+"\u2550"*60+"\u255D\n")
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
        print("\n" + i + " : ")
        
        if i in dictList:
            print("Word found")
            correctWords += 1
            originalInput = originalInput + " " + i
        
        #If word is not in dictionary, 4 options presented. Each option increments its respective summary statistic(s). Also updates original Input variable to output full string afterwards. 
        else:
            while True:
                print("\n\n\u2554"+"\u2550"*40+"\u2557")
                incorrectChoice = input("""
    Incorrect spelling - 
    Would you like to: 
    Ignore (1): 
    Mark as incorrect (2): 
    Add to dictionary (3): 
    Suggest a correct spelling (4): """ + "\n\n\u255A"+"\u2550"*40+"\u255D\n")
                
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
                    print("\nSuggested word is " + suggWord)
                    
                    while True:
                        print("\n\n\u2554"+"\u2550"*40+"\u2557")
                        suggChoice = input("""
        Would you like to : 
        Accept the suggestion (1): 
        Reject the suggestion (2): """ + "\n\n\u255A"+"\u2550"*40+"\u255D\n")
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
    summary = ("\n\u2554"+"\u2550"*60+"\u2557\n"""" 
    Summary Statistics : 
    Total Words : """ + str(totalWords) + """
    Number of Correct Words : """ + str(correctWords) + """
    Number of Incorrect Words : """ + str(incorrectWords) + """
    Number of Added Words : """ + str(addedWords) + """
    Number of Changed Words : """ + str(changedWords) + """
    Date and Time of Spellcheck : """ + str(dateString) + """
    Time Elapsed : """ + str(timeElapsed) + """ Seconds
    Input : """ + originalInput + "\n\n\u255A"+"\u2550"*60+"\u255D\n")
    print(summary)
    print("\n\n\u2554"+"\u2550"*60+"\u2557")
    statsFileName = input("""
    Please enter a filename for the spellcheck file : """ + "\n\n\u255A"+"\u2550"*60+"\u255D\n")
    statsFile = open(statsFileName, "w")
    statsFile.write(summary)
    statsFile.close
    print("\nFile Saved")
    while True:
        print("\n\n\u2554"+"\u2550"*80+"\u2557")
        option = input("""
        Would you like to return to the main menu (1) or Quit (2) : """ + "\n\n\u255A"+"\u2550"*80+"\u255D\n")
        if option == "1":
            break
        elif option == "2":
            print("Exiting program ... ")
            time.sleep(2)
            sys.exit()
        else:
            print("\nInvalid Input - Please only enter either 1 or 2.")
#Main menu - Validated input, only allows for input of 1, 2 or 0.
while True:
    print("\n\u2554"+"\u2550"*40+"\u2557")
    menuChoice = input("""
    Main Menu: 
    Please Select An Option : 
    Enter a sentence (1) : 
    Enter a file name (2) : 
    Exit (0) : 
    """ + "\n\u255A"+"\u2550"*40+"\u255D\n")
    #print("\n\u255A"+"\u2550"*40+"\u255D")
    if menuChoice in ["1", "2", "0"]:
        if menuChoice == "1":
            sentenceCheck()
                

        elif menuChoice == "2":
            valChoice = False
            while valChoice == False:
                print("\n\n\u2554"+"\u2550"*100+"\u2557")
                fNameCheck = input("""
    Please enter the filename that you would like to check, along with the .txt extension : """ + "\n\n\u255A"+"\u2550"*100+"\u255D\n")
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
                        print("\n\u2554"+"\u2550"*40+"\u2557")    
                        choice = input("""
    Would you like to :
    Re-enter the filename (1) : 
    Return to main menu (2) : """ + "\n\n\u255A"+"\u2550"*40+"\u255D\n")
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