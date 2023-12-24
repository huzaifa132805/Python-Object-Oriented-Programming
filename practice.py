class Book:
     def __init__(self,name,book_name,qty):
         self.name = name
         self.book_name = book_name
         self.qty = qty
     def nameOfAuthour(self):
         return f" The Author name is {self.name}"
     def nameOfBook(self):
         return f"The Book Name is {self.book_name}"
     def qtyInStock(self):
         return f"The quantity is {self.qty} "
     def orderForQuantity(self,qtyOrder):
         self.qty += qtyOrder
         return f"The quantity will be {self.qty}"
b1 = Book("Harry","Messi",79)
print(b1.name)
print(b1.orderForQuantity(80))
print(b1.qty)
# This is the method for 
class Author:
    def __init__(self,gender,name,email):
        self.name = name
        self.gender = gender
        self.email = email
    def genderOfAuthour(self):
        return f"The gender of author will be {self.gender}"
    def nameOfAuthour(self):
        return f"The name of authour will be {self.name}"
    def emailOfAuthour(self):
        return f"The email is {self.email}"
b2 = Author("Male","Nolan","realnolan@gmail.com")
print(b2.genderOfAuthour())