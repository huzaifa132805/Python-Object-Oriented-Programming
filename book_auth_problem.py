class Book:
    def __init__(self,name,authour,price,qtyinstock):
        self.name = name
        self.authour = authour
        self.price = price
        self.qtyinstock = qtyinstock
    def getname(self):
        return f"The book name is {self.name}"
    def getauthourname(self):
        return f"The authour name is {self.authour}"
    def qunatity(self):
            return f"The qunatity is {self.qtyinstock}"
    def pric(self):
        return f"The price is set to {self.price}"
    def addauthours(self,au_t):
        return f"This quantity add to the stock {au_t}"
    
class Author:
    def __init__(self,name,email,gender):
        self.name = name
        self.email = email
        self.gender = gender
    def getName(self):
        return f"The author name is {self.name}"
    def mail(self):
        return f"the mail is {self.email}"
    def gen(self):
        return f"The gender will be {self.gender}"


print(Book("Huzaifa","messi",90,100).price())

