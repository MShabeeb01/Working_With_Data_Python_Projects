#Daily Journal Logger

#Step-1: Define the journal file

Journal_File = "daily_journal.txt"
#This creates a variable and stores the file name 

#Step-2: Add a new entry
def add_entry():
    entry = input("Write your journal entry:")
    with open(Journal_File, 'a') as file :
        file.write(entry + '\n')
        print("Entry added successfully")

#Learnings : 
# 1. 'a' means append which will enter the journal at the end without overwriting the old journal.
# 2. file.write this writes the user input into the file and '\n' is written so that the next time the user inputs new journal it starts from a new line .        

#Step-3: View all entries :
def view_entries():
    try:
        with open(Journal_File, 'r') as file:
            content = file.read()
            if content :
                print("\n---Your Journal Entries---")
                print(content)
            else :
                print("No entries found .Start writing today.")
    except FileNotFoundError:
        print("No journal file found . Add an entry first!")

#Step-4: Search entries by keywords 

def search_entries():
    keyword = input("Enter a keyword to search for:").lower()
    try:
        with open(Journal_File,'r') as file :
            content = file.readlines()
            found = False 
            print("\n---Search results---") 
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No journal file found . Add an entry first!")     

#Learnings 
#1. In keyword = input().lower the lower function is used to make the user input case in sensitive .
#2. .readlines() → reads all lines from the file and returns them as a list.
#3. found = False .A flag variable.Initially set to False meaning → we haven’t found the keyword yet.If a matching entry is found, we will change it to True.
#4. for entry in content: Loops through each line (entry) in the journal file.


#Step-5: Display menu
def show_menu():
    print("\n---Daily Journal Logger!---")
    print("1.Add a new entry.")
    print("2.View all entries.")
    print("3.Search entries by keyword.")
    print("4.Exit")

#Step-6: Main program loop 
while True:
    show_menu()
    choice = input("Enter your choice (1-4):").strip() 

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entries()
    elif choice == "4":
        print("Exiting program.Thank you!")
        break
    else :
        print("Invalid choice . Enter a valid choice ")
