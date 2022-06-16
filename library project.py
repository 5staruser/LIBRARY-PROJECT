class library:
    def __init__(self,name,list):
        self.name=name
        self.books=list
        self.lenddict={}
    def displaybooks(self):
        print(f"we have following books in {self.name}")
        for books in self.books:
            print(books)
    def lendbook(self,user,book):
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print(f"you can take book now")
        else:
            print(f"book has already been taken by {self.lenddict[book]}")
    def addbook(self,book):
        self.books.append(book)
        print(f"{book} has been updated in library")
    def returnbook(self,book):
        self.lenddict.pop(book)
if __name__ == '__main__':
    sarthak=library("sarthak library",["web development","pyhton"])
    while(True):
        print(f"welcome to {sarthak.name} enter your choice")
        print("1.displaybooks")
        print("2.lendbook")
        print("3.addbook")
        print("4.returnbook")
        userchoice=int(input())
        if userchoice==1:
            sarthak.displaybooks()
        elif userchoice == 2:
            user=input("enter your name:")
            book=input("enter book which you want")
            sarthak.lendbook(user,book)
        elif userchoice == 3:
            book=input("enter book which you want to add")
            sarthak.addbook(book)
        elif userchoice == 4:
            book=input("enter book which you want to return")
            sarthak.returnbook(book)
        else:
            print("invalid input")
        print("press c to continue and q to quit")
        userchoice2=input()
        if userchoice2=="c":
            continue
        elif userchoice2=="q":
            exit()

