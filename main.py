# class Employee:
#     def __init__(self , name , position , salary , department):
#         self.name = name 
#         self.position = position
#         self.salary = salary
#         self.department = department 

#     def introduce(self):
#         print(f"Name: {self.name}. \nPosition: {self.position}.")


# employee1 = Employee("Jacob" , "UX/UI Designer" , 40_000 , "Art")

# employee1.introduce()




# class Friuts:
#     def __init__(self , name , color , price):
#         self.name = name 
#         self.color = color  
#         self.price = price 

#     def describe(self):
#         print(f"Name: {self.name}. \nColor: {self.color}\nPrice:{self.price}")

# orange = Friuts("Orange" , "Orange" , "2000")
# apple = Friuts("Apple" , "Red" , "3000")

# # orange.describe()

# class Animel:
#     def __init__(self, name , age , gender , height , power , fighting_potential , Energy = 100):
#         self.name = name 
#         self.age = age 
#         self.gender = gender
#         self.height = height
#         self.power = power
#         self.fighting_potential = fighting_potential
#         self.energy = Energy

#     def describe(self):
#         print(f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}\nHeight:{self.height}\nPower:{self.power}\nFighting_potential:{self.fighting_potential}\nStatus:{self.energy}")

#     def sleep(self):
#         self.energy += 10

# orgil = Animel("Orgil","18","prolly gay","1.71m","Buying FUZE TEA","prolly same as buynaa")

# orgil.describe()
# orgil.sleep








#######################

#HOMEWORK


class Menu:
    def __init__(self, name, price, ingredients,healing=5):
        self.name = name 
        self.price = price 
        self.ingredients = ingredients
        self.healing = healing

    def describe(self):
        print(f"Name:{self.name}.")
        print(f"Price:{self.price}.")
        print(f"Ingedients:{self.ingredients}.")
        print(f"Heal:{self.healing}")

    def eat(self):
        print("Tasty!")
        self.healing += 10
        print(self.healing)

pasta = Menu("Pasta", "18'000", "Flour,Cheese,Oil,Sauce")
ramen = Menu("Ramen", "16'000", "Flour,Soup,Beef",)
tsuivan = Menu("Tsuivan", "15'000", "Flour,Onion,Beef")

tsuivan.describe()
pasta.eat()
