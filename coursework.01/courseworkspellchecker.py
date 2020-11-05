import os, time, os.path

dictList = []
with open("englishwords.txt", 'r') as file:
    for line in file:
        dictList.append(line.strip("\n"))
    

    

while True:
    menuChoice = input("Welcome\nPlease type (1) to enter a word, (2) to enter a file name, or (0) to exit : ")
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
                        wordOutput = fileList.split(" ")
                        print(wordOutput)
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
