class calculator:
    
    def add(num1, num2):
        return num1 + num2
    
    def sub(num1, num2):
        return num1 - num2

    def mul(num1, num2):
        return num1 * num2
    
    def div(num1, num2):
        return num1 / num2

def main():

    while True:

        act = input("What do you want to do (add, sub, mul, div, exit) :")
        

        match act:
            case 'add':
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))
                print(f'The sum of {num1} and {num2} = {calculator.add(num1, num2)}')
            case 'sub':
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))
                print(f'The difference of {num1} and {num2} = {calculator.sub(num1, num2)}')
            case 'mul':
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))
                print(f'The multiplication of {num1} and {num2} = {calculator.mul(num1, num2)}')
            case 'div':
                num1 = float(input("Enter the first number:"))
                num2 = float(input("Enter the second number:"))
                if num2 == 0:
                    print("Invalid input, number cannot be divided by zero.")
                else:
                    print(f'The sum of {num1} and {num2} = {calculator.add(num1, num2)}')
            case 'exit':
                print("Calculator has been exited.")
                break
            case _:
                print("Invalid input, enter a valid input.")

if __name__ == '__main__':
    main()
