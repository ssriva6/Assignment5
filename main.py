# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# SSrivatsan,11.16.2020,Created started script
# <YOUR NAME HERE>,<DATE>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = 'todolist.txt'  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# When the program starts, load the any data you have into memory
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# create the table
try:
    strFile = open(objFile,"r")
    for row in strFile:
        strData = row.split(",") #This should return a list
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()} #this is to process the data just like in listing 8 in module 5
        lstTable.append(dicRow)
    strFile.close()
except:
    print("File not found")

# -- Input/Output -- #
# Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 1 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print(lstTable)
        continue
    # Step 2 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        Task = input("Please enter a task:")
        Priority = input( "Please enter a priority:")
        lstTable.append({"Task": Task, "Priority":Priority})
        continue
    # Step 3 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem= input("What would you like to remove?")
        for row in lstTable:
            if row["Task"]== strItem:
                lstTable.remove(row) #this allows you to remove a row if yhe task in the table matches an user input
                print("Row removed!")
                print(lstTable)
            else:
                print( "Row is not found")
                print( lstTable)
        continue
    # Step 4 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Would you like to save your data?")
        save = input("Enter 'y' or 'n':")
        if (save == 'y'):
            strFile = open(objFile,'w')
            for row in lstTable:
                strFile.write(str(row["Task"])+','+str(row["Priority"]+ "\n"))
            strFile.close()
            print("Data saved to file")
        continue
    # Step 5 - Exit program
    elif (strChoice.strip() == '5'):
        print("Thank you for using this program")
        break  # and Exit the program
input()

