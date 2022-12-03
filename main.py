class Book:
    def __init__(self, name, author, yearPublished):
        self.name = name
        self.author = author
        self.yearPublished = yearPublished

    def getName(self):
        return self.name
    
    def getAuthor(self):
        return self.author
    
    def getYearPublished(self):
        return self.yearPublished


