from car import Car
class SportCar(Car):

    def __init__(self, model_name: str, brand_name: str, year: int, price: float, top_speed: int = 0) -> None:
        super().__init__(model_name, brand_name, year, price)
        assert top_speed >= 0, "The top speed of the SportCar is bellow zero"
        self.top_speed = top_speed


# Instanciate the SportCar
        
# sport = SportCar("Supra", "Toyota", 2022, 150000, 250)
# SportCar.instanciate_from_csv()
# sport.pay_rate = 0.6
# print(sport.applyDiscount())
# print(SportCar.all)