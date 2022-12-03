import json

books_string = '''
{
    "books": [
        {
            "name": "A Clockwork Orange",
            "author": "Anthony Burgess",
            "yearPublished": "1962"
        },
        {
            "name": "No Longer Human",
            "author": "Osamu Dazai",
            "yearPublished": "1948"
        },
        {
            "name": "Ender's Game",
            "author": "Orson Scott Card",
            "yearPublished": "1985"
        },
        {
            "name": "Life of Pi",
            "author": "Yann Martel",
            "yearPublished": "2001"
        }
    ]
}
'''

data = json.loads(books_string)
print(data)



class Book:
    def __init__(self, _name, _author, _yearPublished):
        self._name = _name
        self._author = _author
        self._yearPublished = _yearPublished

    def getName(self):
        return self._name

    def setName(self, x):
        self._name = x
    
    def getAuthor(self):
        return self._author
    
    def setAuthor(self, x):
        self._author = x
    
    def getYearPublished(self):
        return self._yearPublished
    
    def setYearPublished(self, x):
        self._yearPublished = x

def showMainMenu():
    print("\n\u001b[90m~\u001b[0m MAIN MENU\n\nYou have arrived at Bing Chilling Library. Would you like to enter?\n(yes / no)\n")
    while True:
        cont = input("\u001b[90m> \u001b[0m").lower()
        if cont == "yes" or cont == "y":
            break
        elif cont == "no" or cont == "n":
            print("\nVery well.\n")
            quit()
        else:
            print("\nThat was not a valid option. Please try again\n(yes / no)\n")
    print("\nVery well. Please select an option.\n(Create / Read / Update / Delete / Exit)\n")
    while True:
        crud = input("\u001b[90m> \u001b[0m").lower()
        # Create
        if crud == "create" or crud == "c":
            print("\nVery well.\n")
            #ask for name
            #ask for author
            #ask for year published
            
        # Read
        elif crud == "read" or crud == "r":
            print("\nVery well.\n")

        # Update
        elif crud == "update" or crud == "u":
            print("\nVery well.\n")

        # Delete
        elif crud == "delete" or crud == "del" or crud == "d":
            print("\nVery well.\n")

        # Exit
        elif crud == "exit" or crud == "e":
            print("\nVery well.\n")
            quit()
        else:
            print("\nThat was not a valid option. Please try again\n(Create / Read / Update / Delete / Exit)\n")

def run():
    showMainMenu()

run()