import math
from decimal import Decimal

# Exercise 1

my_list = ["manzana", "banana", "tomate"]
my_tuple = ("rojo", "verde", "azul")
my_float = 3.4
my_integer = 42
my_decimal = Decimal("10.5")
my_dict = {"nombre": "Juan", "edad": 25, "ciudad": "Bilbao"}

print("Exercise 1: Create a list, tuple, float, integer, decimal and dictionary.")
print(f"list: {my_list}")
print(f"tuple: {my_tuple}")
print(f"float: {my_float}")
print(f"integer: {my_integer}")
print(f"decimal: {my_decimal}")
print(f"dict: {my_dict}\n\n")


# Exercise 2

rounded_float = math.ceil(my_float)
print("Exercise 2: Round yor float up.\n")
print(f"original float: {my_float}")
print(f"rounded up: {rounded_float}\n\n")


# Exercise 3

sqrt_float = math.sqrt(my_float)
print("Exercise 3: Square root of float.\n")
print(f"original float: {my_float}")
print(f"rounded up: {sqrt_float}\n\n")


# Exercise 4

first_dict_element = list(my_dict.items())[0]
print("Exercise 4: Select the first element from your dictionary.\n")
print(f"first element: {first_dict_element}\n\n")


# Exercise 5
second_tuple_element = my_tuple[1]
print("Exercise 5: Select the second element from your tuple.\n")
print(f"second element: {second_tuple_element}\n\n")


# Exercise 6

my_list.append("naranja")
print("Exercise 6: Add element to end of list.\n")
print(f"list after append: {my_list}\n\n")


# Exercise 7

my_list[0] = "pera"
print("Exercise 7: Replace the first element in your list.\n")
print(f"list after replacement: {my_list}\n\n")


# Exercise 8

my_list.sort()
print("Exercise 8: Sort your list alphabetically.\n")
print(f"sorted list: {my_list}\n\n")


# Exercise 9

my_tuple = my_tuple + ("amarillo",)
print("Exercise 9: Reassign to add element tu tuple.\n")
print(f"tuple after reassignment: {my_tuple}\n\n")


