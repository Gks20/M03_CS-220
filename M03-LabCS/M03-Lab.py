class Vehicle():
    def __init__(self, year, make, model, doors, roof, type):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        self.type = type

    def __repr__(self):
        return f"Type = {self.type} Year = {self.year} Model = {self.model} Doors = {self.doors} Roof = {self.roof}"

    Type = input("Please enter the type of vehicle : ")
    Year = input("Enter the year of the vehicle : ")
    Make = input("Enter the make of the vehicle : ")
    Model = input("Enter the model of the vehicle :")
    Doors = input("Enter number of doors : ")
    Roof = input("Enter type of roof (solid or sun roof) :")

    details = ("Vehicle type: " + Type,
               "Year: " + Year,
               "Make: " + Make,
               "Model: " + Model,
               "Number of doors: " + Doors,
               "Type of roof: " + Roof)

    print(details)
