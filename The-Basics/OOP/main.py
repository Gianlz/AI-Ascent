from car import Car
from sportcar import SportCar

# Instanciate

car = Car("GTR R34", "Nissan", 2002, 200000)
# car.model_name = "Civic"
car.pay_rate = 0.6

print(car.model_name)
print(car.price)
print(car.applyDiscount())
print(car.all)


Car.instanciate_from_csv()
print(f"\n{Car.all}")


sportCar = SportCar("Supra", "Toyota", 2022, 150000, 250)
# sportCar.model_name = "Hilux"
sportCar.pay_rate = 0.6
print(sportCar.model_name)
print(sportCar.price)
print(sportCar.applyDiscount())
print(sportCar.appyIncrement(0.7))
print(sportCar.all)

