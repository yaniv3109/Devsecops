##  דוגמה פשוטה של class
# class Person:
#     def __init__(self, name, age):  # Constructor, יוצר אובייקט חדש
#         self.name = name  # תכונה: שם
#         self.age = age    # תכונה: גיל
    
#     def __str__(self):
#         return f'name --> {self.name} , age --> {self.age}'

# per1 = Person("yaniv", 34)
# per2 = Person("moran", 35)
# print(per1)
# print(per2)



### שימוש בהיררכיה של מחלקות (אב ובן במה הזה)

##          Animal
##            |
##     ----------------
##    |                |
##   Dog              Cat


## דוגמה 1
# class Animal:  # מחלקת אב
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# class Dog(Animal):  # מחלקת ילד, יורשת מ- Animal
#     def speak(self):  # מחליפה את הפונקציה speak
#         print(f"{self.name} barks")

# class Cat(Animal):  # מחלקת ילד, יורשת מ- Animal
#     def speak(self):  # מחליפה את הפונקציה speak
#         print(f"{self.name} meows")

# # יצירת אובייקטים
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# dog.speak()  # יצא: Buddy barks
# cat.speak()  # יצא: Whiskers meows



## דוגמה 2
# class Server:
#     def __init__(self, host_name: str, ip: str):
#         self.host_name = host_name
#         self.ip = ip

#     def __str__(self):
#         return f'host name = {self.host_name}, ip = {self.ip}'


# server1 = Server("Server_1", "10.0.0.0")
# server2 = Server("Server_2", "10.1.3.70")

# print(server1)
# print(server2)


# class Webserver(Server):
#     def __init__(self,host_name: str, ip: str, database: str, protocol: str):
#         Server.__init__(self, host_name, ip)
#         self.database = database
#         self.protocol = protocol
    
#     def __str__(self):
#         return f'host name = {self.host_name}, ip = {self.ip}, database = {self.database}, protocol = {self.protocol}'

# webserver1 = Webserver("Server_34", "170.10.12.4", "mongoDB", "https")
# print(webserver1)





## private and public access in classes



## Abstract class based "ABC" and @abstractmethod
# from abc import ABC, abstractmethod

# # מחלקת אב מופשטת (Abstract Base Class)
# class Animal(ABC):
    
#     @abstractmethod
#     def make_sound(self):  # שיטה מופשטת (חייבת להתממש במחלקות ילד)
#         pass
    
#     # המתודה הזו אינה מסומנת כ-abstractmethod, ולכן היא לא חייבת להתממש במחלקות ילד
#     def move(self):  # שיטה רגילה (לא מופשטת)
#         pass

# # מחלקת ילד שמממשת את השיטות המופשטות
# class Dog(Animal):
    
#     def make_sound(self):
#         return "Bark"
    
#     # המתודה move אינה מחויבת למימוש, כי היא לא מופשטת. לכן, אפשר להשאיר אותה גם ללא מימוש.
#     def move(self):
#         return "Runs"

# dog = Dog()

# # קריאה לפונקציות הממומשות
# print(dog.make_sound())  # יצא: Bark
# print(dog.move()) 
