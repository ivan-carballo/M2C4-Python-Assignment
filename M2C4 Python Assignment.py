from decimal import Decimal
import math

#Exercise 1
list = ["list 1", "list 2", "list 3", "list 4"]
tuple_data = ("tuple 1", "tuple 2", "tuple 3")
float = 5.45
integer = 50
decimal_number = Decimal(15.45)
dictionary = {"key 1": ["data 1", "data 2", "data 3", "data 4"],
              "key 2": ["data 5", "data 6", "data 7", "data 8"]}


#Exercise 2
round_float = math.ceil(float)


#Exercise 3
square_float = math.sqrt(float)


#Exercise 4
first_dictionary = dictionary["key 1"]


#Exercise 5
second_tuple = tuple_data[1]


#Exercise 6
list = list + ["Data new"]


#Exercise 7
del list[0]


#Exercise 8
list = sorted(list)


#Exercise 9
tuple_data = tuple_data + ("New element",)