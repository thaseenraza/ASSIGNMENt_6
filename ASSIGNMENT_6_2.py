# Assignment 2
# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color.
#     You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. 
#     It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.



class Dog:
    def __init__(self,name,age,coatcolour):
        self.name = name
        self.age = age
        self.coatcolour = coatcolour
    def description(self):
        print(f" Name of dog Entered is : {self.name} \n Age of Dog Entered is : {self.age}")
    def get_info(self):
        print( f" Coat Colour of Dog entered is : {self.coatcolour}")
class JackRussellTerrier(Dog):
    def __init__(self):
        super().__init__(name,age,coatcolour)
    def family(self):
        print(" Yes JackRusellTerrier is a Family Dog")
    def breed(self):
        print("JackRusellTerrier is from Reverend John Russell")
class bulldog(Dog):
    def __init__(self):
        super().__init__(name,age,coatcolour)
    def size(self):
        print("Yes Bull dogs are Medium size")
    def span(self):
        print("Bull Dogs have a life span of 8-10 Years")
name = input("Enter the Name of the Dog : ")
age = int(input("Enter the Age of the Dog : "))
coatcolour = input("Enter the coatcolour of the Dog : ")


 
Dog_obj = Dog(name,age,coatcolour)          

Dog_obj.description()                                         #For Description

Dog_obj.get_info()                                            #For Get_Info

JackRussellTerrier_obj = JackRussellTerrier()                 #For JackRussellTerrier
JackRussellTerrier_obj.description()
JackRussellTerrier_obj.get_info()
JackRussellTerrier_obj.family()
JackRussellTerrier_obj.breed()


bulldog_obj = bulldog()                                        #For Bull Dog
bulldog_obj.description()
bulldog_obj.get_info()
bulldog_obj.size()
bulldog_obj.span()