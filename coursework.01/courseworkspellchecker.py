import os, time, os.path
def intValidator(choice):
    try:
        choice = int(choice)
    except:
        print("Invalid input entered.")
    return choice
    
def sentenceCheck():
    checkSentence = input("\nPlease enter the sentence you wish to check : ")
    sentenceList = []
    sentenceList = checkSentence
    wordOutput = sentenceList.split(" ")
    print(wordOutput)
    return(checkSentence)

def fileCheck():
    fNameCheck = input("\nPlease enter the filename that you would like to check, along with the .txt extension : ")
    try:
        fileList = []
        with open(fNameCheck, 'r') as file:
            fileList = file.read()
            wordOutput = fileList.split(" ")
            print(wordOutput)
        
    
    except FileNotFoundError:
        print("\nFile does not exist.")
        return(fileCheck())

def menuSystem():

    menuChoice = input("Welcome\nPlease type (1) to enter a word, (2) to enter a file name, or (0) to exit : ")
    if menuChoice in ["1", "2", "0"]:
        if menuChoice == "1":
            sentence = sentenceCheck()
            print(sentence)

        elif menuChoice == "2":
            fileTest = fileCheck()
            print(fileTest)

        elif menuChoice == "0":
            print("Exiting program ... ")
            time.sleep(2)
            os._exit
    
    else:
        print("\nPlease only enter either 1, 2 or 3")
        return menuSystem()
menuSystem()