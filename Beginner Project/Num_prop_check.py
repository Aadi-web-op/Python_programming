from math import factorial
class Prop_checker:
    def even_odd(num):
        if num % 2 == 0:
            return " IS EVEN"
        else:
            return " IS ODD"
        
    def is_prime(num):
        if num <= 0 or num == 1:
            return " IS NOT PRIME"
        
        elif num > 1:
            for i in range(2,int(num ** 0.5) + 1):
                if num % i == 0:
                    return " IS NOT PRIME"
            return " IS PRIME"
        
    def fact(num):
        return factorial(num)
        

    
def main():
    while True:

        inp = int(input('''MENU
            Check if number is Even or Odd --> 1
            Check if number is Prime --> 2
            Find factorial --> 3
            Exit --> 4
        '''))
       

        match inp:

            case 1:
                num = int(input("Enter the number :"))
                print(f'The number{Prop_checker.even_odd(num)}')
            case 2:
                num = int(input("Enter the number :"))
                print(f'The number{Prop_checker.is_prime(num)}')
            case 3:
                num = int(input("Enter the number :"))
                print(f'The factorial of {num} = {Prop_checker.fact(num)}')
            case 4:
                print("BYE")
                break
if __name__ == '__main__':
    main()
