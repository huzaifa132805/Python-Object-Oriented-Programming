#“If it looks like a duck and quacks like a duck, it’s a duck”
# Python program to demonstrate 
# duck typing 


class Bird: 
	def fly(self): 
		print("fly with wings") 

class Airplane: 
	def fly(self): 
		print("fly with fuel") 

class Fish: 
	def fly(self): 
		print("fish swim in sea") 

# Attributes having same name are 
# considered as duck typing 
for obj in Bird(), Airplane(), Fish(): 
	print(obj.fly()) 

