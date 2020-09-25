from datetime import date
from os import system

def clearScreen():
    system('cls')
    


class library:
    books = []
    lend = {}

    def __init__(self,nameOfLibrary):
        self.nameOfLibrary = nameOfLibrary
    
    def lendBook(self,owner,bookName):
        #This manages the out flow of books
        self.bookName = bookName.lower()
        self.owner = owner.lower()
        print("Giving You Your Book")
        print(f"Prosseing book Title - {bookName}")
        if(bookName in self.books):
            print("Book was Found")
            if(bookName in self.lend):
                print("The Book {} is borrowed by {}\nyou can borrow it once its back".format(bookName,self.lend.get(bookName)))
                return None            
            print("Adding it to your account")
            self.lend[bookName]=owner
            print("Book have been sucessfull added")
            print("Recipt - \n book - {} \n borrow on - {} \n borrow by - {}".format(bookName,date.today().strftime("%B %d, %Y"),owner))
            print("Thank You {} for using our servicies".format(owner))
            return None

        else:
            print("sorry there was no book with the title - {}".format(bookName))
            return None
    
    def return_books(self,bookName,owner):
        #This manages the returen book feature
        self.bookName = bookName.lower()
        self.owner = owner.lower()
        print("Pls wait while you book gets validated")
        if((bookName in self.books) and (bookName in self.lend)):
            print("Book has been validated")
            if(self.lend.get(bookName) != owner):
                print("The book was not borrwed by anyone with the name {}".format(owner))
                return None
            else:
                print("Prosseing you book now")
                del self.lend[bookName]
                print("Your system have recived you book \nThx for using {} Library".format(self.nameOfLibrary))
                return None
        elif(bookName not in self.lend and bookName in self.books):
            print("This is book was not borrowed yet")
            return None
        elif(bookName not in self.books):
            print("This is no book with the name {}".format(bookName))
            return None
        else:
            print("there was an unexpected error pls repot it")
            return None
            #aad a auto maticlay repot

    @classmethod
    def DisplayAllBooks(cls):
        outOfLibrary = []
        bookId = 1
        print("**[ These are the book you can borrow right now ]**\n")
        for book in cls.books:
            if(book in cls.lend):
                outOfLibrary.append(book)
            else:
                print("  {}) {}".format(bookId,book))
        print("\n** Here are this of books borrowed by others **\n")
        for items in outOfLibrary:
            print("  {}){}".format(outOfLibrary.index(items)+1,items))
    
    @classmethod
    def addBooks(cls,newBook):
        cls.newBook = newBook.lower()
        print("New Book is - "+newBook)
        print("If there are any correction pls write the new name bellow\njust hit enter to no change")
        if(newBook in cls.books or (newBook == "" or newBook == " ")):
            print("This book already exits or is an invalid name\nyou donation have been cansiled")
            return
        else:
            cls.books.append(newBook)
        print("You book have been added to library \nThx for you donation")


if __name__ == '__main__':
    helpDesk = {
        "borrow":"To Rent or Borrow the book from library",
        "donate":"To Donate a book to library",
        "show":"To list all the books avalible in the library",
        "retuen":"To returne a book which you have borrowed",
        "clear":"To clear screen"
    }
    MyLib = library("The Text Library")
    print("Welcom to {},\nuse -h for help".format(MyLib.nameOfLibrary))
    while True:
               
        task = input(" :").lower()
        if(task=="-h"):
            print("Here are you option for help")
            for helpOption in helpDesk:
                print("command\t{}\t{}".format(helpOption, helpDesk.get(helpOption)))
                
        elif(task=="clear"):
            clearScreen()

        elif(task=="donate"):
            MyLib.addBooks(newBook=input("Enter The Name of the BOOK : "))
        
        elif(task=="retuen"):
            MyLib.return_books(input("Name of the book you are returning : "), input("Name you borrowed with: "))

        elif(task=="show"):
            MyLib.DisplayAllBooks()
        
        elif(task=="borrow"):
            MyLib.lendBook(input("Your Name : "),input("Book You want to borrow : "))

        else:
            print("Command not found")