'''
Exercise Summary:
1.) variable = variable[:2] Strips the last two characters in the string
2.) yield statement suspends a functions execution & sends a value to the caller
    .. but retains state to enable the function to resume wher it left off
    .. this allows the code to produce a series of values over time
'''

from objects import Book, Author, Authors

def main():
    print("The Authors Tester program")
    print()
    
    #Create author list of author first & last names
    author1 = Author("Mark", "Twain")       
    author2 = Author("Charles", "Warner")
    #Authors set to Authors class
    authors = Authors()
    #Add authors1 & 2 to authors class value
    authors.add(author1)
    authors.add(author2)
    #Create book variable with a string variable @ authors class variable
    book = Book("The Gilded Age", authors)

    # display the book data
    print("BOOK DATA - SINGLE LINE")
    print(book)
    print()

    print("BOOK DATA - MUTLIPLE LINES")

    if authors.count < 2:
        print("Author:  ", book.authors)
    else:
        print("Authors:   ", book.authors)
    print()

    print("Authors")
    for author in authors:
        print(author)
        
if __name__ == "__main__":
    main()
