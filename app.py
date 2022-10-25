# Nate Orona

# MO3 Lab - Car Builder

# This program uses a class "Vehicle" and two methods 
# "print_car()" and "get_input()" to take user input
# for the details of a car and print those details in
# a readable fashion

class Vehicle:
    def __init__(self, year, make, model, doors, roof):
        self.year = year;
        self.make = make;
        self.model = model;
        self.doors = doors;
        self.roof = roof;
        
    def print_car(self):
        make = self.make;
        year = self.year;
        model = self.model;
        doors = self.doors;
        roof = self.roof;
        print(f"Make: {make}")
        print(f"Year: {year}")
        print(f"Model: {model}")
        print(f"Doors: {doors}")
        print(f"Roof: {roof}")

    def get_input(self):
        make = input('Make of the car: ');
        model = input('Model of the car: ');
        year = input('What year was the car built? ');
        doors = input('2 or 4 doors? ');
        roof = input('Solid or sunroof? ');
        new_car = Vehicle(year, make, model, doors, roof);
        return new_car.print_car();

car = Vehicle(1992, 'dudley', 'maurice', 2, 'solid');

print(car.get_input())
