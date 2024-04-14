from dataclasses import dataclass

# must be coded before Book class, as Book class has an Authors type hint
# isn't a data class because has an attribute that's a list
class Authors:
    # Initiate authors list
    def __init__(self):
        self.__list = []

    # add authors to authors list
    def add(self, author):
        self.__list.append(author)

    #Gets the Length of the list
    @property
    def count(self):
        return len(self.__list)
    
    # Creates a string of authors along with a ", " spacer
    def __str__(self):
        author_str = ""
        for author in self.__list:
            author_str += str(author) + ", "
        author_str = author_str[:-2]  # strip last ", " tool removes the last spacer of the string
        return author_str
    
    def __iter__(self):
        for author in self.__list:
            yield author #Executes the function to display multiple results 
    
@dataclass
class Book:
    title:str = ""
    authors:Authors = None
    #Returns the books class as a description
    def getDescription(self):
        return f"{self.title} by {self.authors}"
    
@dataclass
class Author:
    firstName:str = ""
    lastName:str = ""

    def __str__(self):
        return f"{self.firstName} {self.lastName}"




