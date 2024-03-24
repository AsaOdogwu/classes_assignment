# class Human:
#     def __init__(self, country,gender) -> None :
#         self.country =country
#         self.gender = gender

#     def sleep(self):
#         return f"go to sleep"
# kosi = Human("Nigeria","Female")
# print(kosi.sleep())
# print(kosi.country)

# david = Human("Nigeria","Male")
# print(david.gender)
# david.gender = "female"
# print(david.gender)

# # Classwork
class Restaurant:
    """A simple attempt to describe my class Restaurant"""
    def __init__(self, name, cuisine_type)-> None:
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # def describe_restaurant(self):
    #     return f"our restaurant name is {self.name} and we serve quality{self.cuisine_type}"
    def open_restaurant(self):
        print (f"our restaurant{self.name} is open")
    
    def set_number_served(self,number):
        self.number_served = number
        print(f"The value for the number is {self.number_served} ")
    def increment_number_served(self,num):
        self.increment_number_served = +num
        print(f"The value should be increased by {self.increment_number_served}")
restaurant =Restaurant("Odi-oku","international-dishes")
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(15)
print(restaurant.number_served)
restaurant.increment_number_served(30)
print(restaurant.increment_number_served)

# restaurant.client_served(50)


# print(restaurant.name)
# print(restaurant.cuisine_type)

# restaurant_1 = Restaurant("ntachi_osa","chicken pepperoni")
# restaurant_1.describe_restaurant()
# restaurant_2 = Restaurant("Roots","spinach-rice")
# restaurant_2.describe_restaurant()
# restaurant_3 = Restaurant("pinky","sauced-turkerani")
# restaurant_3.describe_restaurant()


class IceCreamStand(Restaurant):
    def __init__(self,name,cuisine_type) -> None:
        super().__init__(name,cuisine_type)
        self.flavors = ["strawberry","vanilla","chocolate","mint","coconut"]
    def display_flavors(self):
        print(f"We have {self.flavors} ice-cream available")
restaurant =IceCreamStand("chops","spaghetti bolognese")
restaurant.display_flavors()




class User:
    """A simple attempt to describe my class User"""
    def __init__(self, first_name, last_name,age,gender)-> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        self.gender = gender
        self.login_attempts = 0

        
    def describe_user(self):
        print (f"my first_name is {self.first_name} and my last _name is {self.last_name}, i'm {self.age}years old and a {self.gender}")
    def greet_user(self):
        print (f"Hello {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The login attempts made so far is {self.login_attempts} ")
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The login attempts made so far is {self.login_attempts} ")
user1 = User("kosi","jideofor",21,"female")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

class Admin(User):
    def __init__(self, first_name, last_name, age, gender) -> None:
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Priviledges()
        self.show_privileges = self.privileges.show_privileges()
    




class Priviledges (Admin):
    def __init__(self) -> None:
        self.privileges = ["add-post","delete-post","ban-user"]
    def show_privileges(self):
        print(f"the privilege{self.privileges},successfully !")

admin = Admin("kosi","jideofor",21,"female")
admin.show_privileges



        


# hello = User ("Fortune","Okolo",45,"male")
# hello.describe_user()
# hi = User ("otamiemie","Isong",35,"she-male")
# hi.describe_user()
# hey = User("sanusi","lamido",98,"male-she")
# hey.describe_user()


# class Car:
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
        
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#     def read_odometer(self,mileage:int):
#       if mileage > self.odometer_reading:
#        self.odometer_reading = mileage

#     def update_odometer(self,mileage:int):
#        if mileage > self.odometer_reading:
#            self.odometer_reading = mileage

# kosi_car = Car('audi', 'a4', 2019)
# print(kosi_car.get_descriptive_name())  

# kosi_car.odometer_reading = 50
# kosi_car.read_odometer()

# kosi_car.update_odometer(570)
# kosi_car.drive_car()
    

    



