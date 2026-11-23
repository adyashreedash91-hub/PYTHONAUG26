# **Question 1 – Book Details**
# Create a `Book` class with:
# - Book name
# - Author name
# - Price
# Use a constructor to initialize the values and a method to display book details.

# class Book:
#     def __init__(self, book_name, author_name, price):
#         self.book_name = book_name
#         self.author_name = author_name
#         self.price = price

#     def display(self):
#         print("Book Name:", self.book_name)
#         print("Author Name:", self.author_name)
#         print("Price:", self.price)

# b1 = Book("Harry Potter", "Adya", 500)
# b1.display()

# **Question 2 – Rectangle**
# Create a `Rectangle` class with length and width.
# Create two methods:
# - `area()` – Calculate area.
# - `perimeter()` – Calculate perimeter.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def area(self):
#         print("Area of Rectangle:", self.length * self.width)
#     def perimeter(self):
#         print("Perimeter of Rectangle:", 2 * (self.length + self.width))


# r1 = Rectangle(10, 5)
# r1.area()
# r1.perimeter()

# **Question 3 – Movie Ticket**

# Create a `MovieTicket` class with movie name and ticket price.
# Create methods to:
# - Display movie details.
# - Calculate total price for multiple tickets.

# class MovieTicket:
#     def __init__(self, movie_name, ticket_price):
#         self.movie_name = movie_name
#         self.ticket_price = ticket_price

#     def display(self):
#         print("Movie Name:", self.movie_name)
#         print("Ticket Price:", self.ticket_price)

#     def total_price(self, quantity):
#         total = self.ticket_price * quantity
#         print("Number of Tickets:", quantity)
#         print("Total Price:", total)

# m1 = MovieTicket("Pushpa 2", 200)
# m1.display()
# m1.total_price(3)

# **Question 4 – Electricity Bill**
# Create an `ElectricityBill` class with customer name and units consumed.
# Calculate the bill using ₹5 per unit.

# class ElectricityBill:
#     def __init__(self, customer_name, units_consumed):
#         self.customer_name = customer_name
#         self.units_consumed = units_consumed
#     def calculate_bill(self):
#         bill = self.units_consumed * 5
#         print("Customer Name:", self.customer_name)
#         print("Units Consumed:", self.units_consumed)
#         print("Electricity Bill: Rs.", bill)

# e1 = ElectricityBill("Adyashree", 100)
# e1.calculate_bill()


# **Question 5 – Shopping Cart**
# Create a `ShoppingCart` class with product name, price, and quantity.
# Create methods to:
# - Display product details.
# - Calculate total price.
# - Apply a 10% discount if the total price is above ₹5,000.



# class ShoppingCart:
#     def __init__(self, product_name, price, quantity):
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity
        
#     def display(self):
#         print("Product Name:", self.product_name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)

#     def calculate_total(self):
#         total = self.price * self.quantity

#         if total > 5000:
#             discount = total * 10 / 100
#             final_price = total - discount

#             print("Total Price: Rs.", total)
#             print("Discount: Rs.", discount)
#             print("Final Price: Rs.", final_price)
#         else:
#             print("Total Price: Rs.", total)
#             print("No Discount Applied")

# s1 = ShoppingCart("Laptop", 3000, 2)
# s1.display()
# s1.calculate_total()