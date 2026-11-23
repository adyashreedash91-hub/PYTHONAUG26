# 1. Encapsulation – Product Management

# Create a Product class with a private price attribute. Create methods to update and display the price.


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price  
    
#     def update_price(self, new_price):
#         self.__price = new_price
#         print("Price updated successfully!")

    
#     def display_price(self):
#         print("Product Name:", self.name)
#         print("Product Price:", self.__price)


# p1 = Product("tablet", 50000)
# p1.display_price()
# p1.update_price(45000)
# p1.display_price()


# 2. Single Inheritance – Library

# Create a `Library` parent class with a `library_info()` method. Create a `BookSection` child class with its own `display_books()` method.


# class Library:
#     def library_info(self):
#         print("Welcome to Central Library")
#         print("Library Timing: 9 AM to 5 PM")


# class BookSection(Library):
#     def display_books(self):
#         print("Available Books:")
#         print("1. Harry Potter")
#         print("2. Wings of Fire")
#         print("3. Data Structures")

# b1 = BookSection()
# b1.library_info()
# b1.display_books()


# 3. Multiple Inheritance – Smart Home

# Create two parent classes, `Light` and `Fan`. Create a child class `SmartHome` that inherits from both.

# class Light:
#     def light_on(self):
#         print("Light is ON")

#     def light_off(self):
#         print("Light is OFF")



# class Fan:
#     def fan_on(self):
#         print("Fan is ON")

#     def fan_off(self):
#         print("Fan is OFF")



# class SmartHome(Light, Fan):
#     def home_status(self):
#         print("Smart Home System")


# s1 = SmartHome()
# s1.home_status()
# s1.light_on()
# s1.light_off()
# s1.fan_on()
# s1.fan_off()

# 4. Multilevel Inheritance – Education
# Create three classes: `Education`, `School`, and `OnlineSchool`. Implement multilevel inheritance and call all inherited methods.


# class Education:
#     def education_info(self):
#         print("Education is important for everyone.")


# class School(Education):
#     def school_info(self):
#         print("School Name: DAV Public School")
#         print("School Location: Bhubaneswar")


# class OnlineSchool(School):
#     def online_info(self):
#         print("Online Classes are available.")
#         print("Platform: Google Meet")


# s1 = OnlineSchool()
# s1.education_info()
# s1.school_info()
# s1.online_info()

# 5. Hierarchical Inheritance – Vehicles

# Create a parent class `Vehicle` and child classes `Car`, `Bus`, and `Bike`. Each child should have its own method.


# class Vehicle:
#     def vehicle_info(self):
#         print("This is a Vehicle.")


# class Car(Vehicle):
#     def car_info(self):
#         print("Car: Hyundai Creta")
#         print("Car has 4 wheels.")


# class Bus(Vehicle):
#     def bus_info(self):
#         print("Bus: Volvo Bus")
#         print("Bus is used for public transport.")


# class Bike(Vehicle):
#     def bike_info(self):
#         print("Bike: Royal Enfield")
#         print("Bike has 2 wheels.")

# c1 = Car()
# b1 = Bus()
# b2 = Bike()

# c1.vehicle_info()
# c1.car_info()
# b1.vehicle_info()
# b1.bus_info()
# b2.vehicle_info()
# b2.bike_info()


# 6. Hybrid Inheritance – Smart Devices

# Create a parent class `Device`, two child classes `Computer` and `Television`, and a final class `SmartDevice` inheriting from both.


# class Device:
#     def device_info(self):
#         print("This is an electronic device.")


# class Computer(Device):
#     def computer_info(self):
#         print("Device: Computer")
#         print("Computer is used for programming.")


# class Television(Device):
#     def television_info(self):
#         print("Device: Television")
#         print("Television is used for entertainment.")


# class SmartDevice(Computer, Television):
#     def smart_info(self):
#         print("Smart Device supports multiple features.")


# s1 = SmartDevice()

# s1.device_info()
# s1.computer_info()
# s1.television_info()
# s1.smart_info()

# 7. Polymorphism – Notification System

# Create `EmailNotification`, `SMSNotification`, and `PushNotification` classes. Each class should have a `send()` method with different messages.


# class EmailNotification:
#     def send(self):
#         print("Sending notification through Email.")

# class SMSNotification:
#     def send(self):
#         print("Sending notification through SMS.")

# class PushNotification:
#     def send(self):
#         print("Sending notification through Push Notification.")

# e1 = EmailNotification()
# s1 = SMSNotification()
# p1 = PushNotification()

# e1.send()
# s1.send()
# p1.send()

# 8. Abstraction – Online Booking
# Create an abstract class `Booking` with an abstract method `confirm_booking()`. Implement it in `HotelBooking` and `FlightBooking`.

# from abc import ABC, abstractmethod
# class Booking(ABC):

#     @abstractmethod
#     def confirm_booking(self):
#         pass

# class HotelBooking(Booking):
#     def confirm_booking(self):
#         print("Hotel booking confirmed successfully!")

# class FlightBooking(Booking):
#     def confirm_booking(self):
#         print("Flight booking confirmed successfully!")


# h1 = HotelBooking()
# f1 = FlightBooking()

# h1.confirm_booking()
# f1.confirm_booking()

