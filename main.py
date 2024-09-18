class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}
    def displayBooks(self):
        print("We have the following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
        else:
            print("Book is already being used")
    def addBook(self,book):
        self.bookslist.append(book)
        print("Book has been added to books list")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__=='__main__':
    books = Library(['Python','Rich Dad','Poor Dad','Harry Potter','C++ Basics','Algorithms by CLRS'],"Let's Upskill")
    while(True):
        print("Welcome to the {books.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input("Enter ur choice")
        if user_choice not in['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:user_choice = int(user_choice)
        if user_choice == 1:
            books.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book u want to lend:")
            user = ("Enter ur name:")
            books.lendBook(user,book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            books.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 =="q":
                exit()
            elif user_choice2 == "c":
                continue