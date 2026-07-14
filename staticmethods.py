class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
            return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Cleaner"]
        return position in valid_positions
        
employee1 = Employee("Mr. Krabs", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

# STATIC METHOD     (Done on the class as a whole)
print(Employee.is_valid_position("Cook"))

#INSTANCE METHOD    (Done on specific objects)
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

