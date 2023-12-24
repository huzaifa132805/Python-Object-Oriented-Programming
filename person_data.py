class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def details(self):
        return f"{self.name} age is {self.age}\n{self.name} Height is {self.height}\n{self.name} Weight is {self.weight} Kgs"
b1 = Person("Raza",21,"5'7",80)
print(b1.details())