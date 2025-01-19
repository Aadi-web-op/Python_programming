class Car:
    def __init__(self, model, brand, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"The {self.model} model belongs to {self.brand} and its price is {self.price} INR"


if __name__ == "__main__":
    print("....Welcome to the car showroom....")

    showroom = []

    while True:
        print('''
        To add car --> 1
        To display cars --> 2
        To exit --> 3
        ''')

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                
                model = input("Enter the model: ")
                brand = input("Enter the brand: ")
                price = float(input("Enter the price: "))

                car = Car(model, brand, price)  
                showroom.append(car)
                print("The car has been added.")

            case 2:
                if not showroom:
                    print("No cars in the showroom yet.")
                else:
                    print("\nList of Cars in the Showroom:")
                    for i, car in enumerate(showroom, 1):
                        print(f"Car {i}: {car.display_info()}")

            case 3:
                print("Bye")
                break

            case _:
                print("Invalid choice! Please try again.")
