'''
Create a script which demonstrates Pickling and error control
Change Log (Who, When, What)
GSEARS, 11-20-2019, Created Script
GSEARS, 11-20-2019, Fixed local/global variable issue with loading from saved file
Gsears, 11-20-2019, added try/except statements to the removeItem() function
'''
import pickle

# Data
lstWords = [] #list to contain list of terms provided by the user
wordList = [] #temporary list used as an output from function for reassignment to lstWords
choice = '' #string used to capture selection from mainMenu()
dataFile = 'WordList.dat' # file name used for storing list


# Processing

# Collect Input into List via function
def collectWords():
    """Collects terms to be added to the word list.
    :return: string newWord"""
    newWord = input('Enter the next term in your list:')
    return newWord

def mainMenu():
    """Displays the main menu for the application, and choices which can be selected
    to execute different blocks of code.
    :return: nothing"""
    print('''Select an Option from the Items below:
    1) Add word to the list
    2) Write list to file
    3) Read words from list
    4) Remove words from list
    5) Show current list
    6) Exit Program
    
    ''')

def writeFile(wordList,dataFile):
    """Writes data collected into the word list to the designated file.
    :param: wordlist - a list of terms to be added to file
    :param: dataFile - the name of the file which is being written to.
    :return: none"""
    f = open(dataFile,"wb")
    pickle.dump(wordList,f)
    f.close()
    print()
    print('Your data has been written to a binary file named "WordList.dat"')
    print()

def readFile(dataFile):
    """Reads data from stored binary file 'WordList.dat'
    :param: datafile (filename) used to designate were to read from.
    :return: lstWords (list) of terms read from dataFile"""
    try:
        f = open(dataFile, "rb")
        lstWords = pickle.load(f)
        f.close()
        print()
        print(lstWords)
        print()
        return lstWords
    except:
        f = open(dataFile, "ab")
        lstWords = []
        f.close()
        return lstWords


def removeItem(term,lstWords):
    """Removes items from the active list.
    :param: term (string) to be added to lstWords
    :param: lstWords(list) container for terms provided to the list.
    :return: lstWords (list) """
    try:
        lstWords.remove(term)
    except ValueError:
        print()
        print('The term,', term, 'is not in the list. Check your spelling and punctuation.')
    return lstWords


# Presentation


# Main Script
lstWords = readFile(dataFile)
while True:
    mainMenu()
    choice = int(input('Please select a number between 1 and 6:'))
    try:
        if choice == 1:
            lstWords.append(collectWords())
            print(lstWords)
        elif choice == 2:
            writeFile(lstWords, dataFile)
        elif choice == 3:
            lstWords = readFile(dataFile)
        elif choice == 4:
            print(lstWords)
            term = input('What term do you want to remove?')
            lstWords = removeItem(term, lstWords)
            print()
            print(lstWords)
        elif choice == 5:
            print('Your current list is:')
            print()
            print(lstWords)
        elif choice == 6:
            print('Thank you.')
            break
        else:
            print()
            raise
    except:
        print('You need to make a section between 1 and 6')
        print()

