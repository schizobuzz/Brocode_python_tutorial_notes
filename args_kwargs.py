#Non-keyword arguments
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mr." "Spongebob", "Harold", "Squarepants", "VII")

#Keyword arguments

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", city="Fake City", state="Fake State", zip="12345")