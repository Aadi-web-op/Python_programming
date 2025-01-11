class Temp_converter:
    def from_c(celsius):
        farenheit = (celsius * (9 / 5 )) + 32
        kelvin = celsius + 273.15
        return farenheit,kelvin
    
    def from_f(farenheit):
        celsius = 5 / 9 * (farenheit - 32)
        kelvin = (farenheit - 32) * 5 / 9 + 273.15
        return kelvin,celsius
    
    def from_k(kelvin):
        farenheit = (kelvin - 273.15) * 9 / 5 + 32
        celsius = kelvin - 273.15
        return farenheit,celsius

    
def main():
    while True:

        inp = int(input('''MENU
            Convert Celsius to Fahrenheit and Kelvin --> 1
            Convert Fahrenheit to Celsius and Kelvin --> 2
            Convert Kelvin to Celsius and Fahrenheit --> 3
            Exit --> 4
        '''))
        temp = float(input("Enter the temperature :"))

        match inp:

            case 1:
                converted = Temp_converter.from_c(temp)
                print(f'{temp}C is equal to {converted[0]}F and {converted[1]}K ')
            case 2:
                converted = Temp_converter.from_f(temp)
                print(f'{temp}F is equal to {converted[0]}K and {converted[1]}C ')
            case 3:
                converted = Temp_converter.from_k(temp)
                print(f'{temp}K is equal to {converted[0]}F and {converted[1]}C ')
            case 4:
                print("BYE")
                break
if __name__ == '__main__':
    main()
