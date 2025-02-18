class Car:
    def __init__(self, brand, model, year):
        
        if not isinstance(year, int) or year < 1886:  
            raise ValueError("Year must be a valid integer and no earlier than 1886.")
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
      
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"

    def is_classic(self):
       
        current_year = 2025  
        return current_year - self.year > 20

    def __str__(self):
       
        return f"Car({self.brand}, {self.model}, {self.year})"

    def compare_year(self, other_car):
       
        if not isinstance(other_car, Car):
            raise TypeError("Comparison must be between two Car objects.")
        if self.year > other_car.year:
            return f"{self.model} is newer than {other_car.model}."
        elif self.year < other_car.year:
            return f"{self.model} is older than {other_car.model}."
        else:
            return f"Both {self.model} and {other_car.model} are from the same year."


car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Chevrolet", "Camaro", 2015)


print("Car 1 Information:")
print(car1.display_info())

print("\nCar 2 Information:")
print(car2.display_info())


print("\nIs Car 1 a classic?", "Yes" if car1.is_classic() else "No")
print("Is Car 2 a classic?", "Yes" if car2.is_classic() else "No")


print("\nYear Comparison:")
print(car1.compare_year(car2))
