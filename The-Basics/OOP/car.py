import csv


class Car:
    # Class atributes
    pay_rate = 1  # Set to 1 because means the full price
    all = []

    # Constructor (Instance atributes)
    def __init__(self, model_name: str, brand_name: str, year: int, price: float) -> None:
        # Assertion (Use only in development for debbugin)
        assert year > 0, f"Year {year} is bellow zero"

        # assign self values for the attributes
        self.__model_name = model_name
        self.brand_name = brand_name
        self.year = year
        # Only for the OOP learning
        self.__price = price

        # Saving instances in list
        Car.all.append(self)

    # Creating getter and setter for model_name
        
    # Getter
        
    @property
    def price(self):
        return self.__price
    
    @property
    def model_name(self):
        return self.__model_name
    
    # Setter
    @model_name.setter
    def model_name(self, value):
        if len(value) > 10:
            raise Exception("Model name is too long (MAX: 10 char)")
        else:
            self.__model_name = value

    # Method to return formated String with the values
    def toString(self) -> str:
        return f"Model: {self.model_name} Brand: {self.brand_name} Year: {self.year} Price: {self.price:,.0f}"

    def applyDiscount(self) -> str:
        self.__price = self.__price * self.pay_rate
        return f"Price after Discount: {self.__price:,.0f}$ (rounded)"  # Can use Car.pay_rate, if the payrate are going to change equals for all the cars.
    
    def appyIncrement(self, increment_value) -> float:
        self.__price += self.__price + increment_value
        return f"Price after Increment: {self.__price:,.0f}$ (rounded)"

    # Magic method to retrieve the instances
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.model_name, self.brand_name, self.year, self.price}"

    # Method to instantiate from a csv

    @classmethod  # Defining as class method using de decorator @classmethod, and passing the class insted instance in arguments
    def instanciate_from_csv(cls):
        with open('cars.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            assert int(item.get('year')) > 0, f"Year (in excel) {item.get('year')} is bellow zero"
            assert float(item.get('price')) > 0, f"Price (in excel) {item.get('price')} is bellow zero"
            Car(
                
                model_name=item.get('model_name'),
                brand_name=item.get('brand_name'),
                year=int(item.get('year')),
                price=float(item.get('price'))
            )





# def main():

#     # Instanciate the class
#     car1 = Car("GTR R34", "Nissan", 2002, 200000)
#     car2 = Car("Civic", "Honda", 2021, 150000)

#     # Calling toString
#     print(car1.toString())
#     print(car2.toString())

#     # set the individual rates for each car
#     car1.pay_rate = 0.8
#     car2.pay_rate = 0.7

#     # Apply the discount
#     print(car1.applyDiscount())
#     print(car2.applyDiscount())

#     # Iterating the instances list to get the name
#     print("\n")
#     for instance in Car.all:
#         print(instance.model_name)

#     # The same thing but using the magic method __repr__ to be more specific
#     print("\nUsing __repr__")
#     print(Car.all)

#     # Instanciate from csv
#     Car.instanciate_from_csv()
#     print(Car.all)
# if __name__ == "__main__":
#     main()