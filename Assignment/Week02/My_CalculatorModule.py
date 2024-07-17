import sys

class myCalculator:
    def __init__(self):
        self.res = 0
    
    def add(self, a, b):
        self.res = a + b
    
    def sub(self, a, b):
        self.res = a - b
    
    def multiply(self, a, b):
        self.res = a * b
    
    def division(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError
            self.res = a / b
        except ZeroDivisionError as e:
            print(e)
    
    def display_result(self):
        print(f"Result: {self.res:.2f}")



class my_ScientificCalculator(myCalculator):
    def power(self, base, exponent):
        self.res = base ** exponent



def checking_valid_choice():
    while True:
        try:
            choice = int(input("Enter your choice between (1/2/3/4/5/6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Invalid choice! Please enter a valid option from the menu.")

        except ValueError:
            print("Invalid input! Please enter a number.")


def user_Choice(choice):
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    calc_variable = myCalculator()

    if choice == 1:
        calc_variable.add(n1, n2)
    elif choice == 2:
        calc_variable.sub(n1, n2)
    elif choice == 3:
        calc_variable.multiply(n1, n2)
    elif choice == 4:
        calc_variable.division(n1, n2)
    elif choice == 5:
        calc_variable = my_ScientificCalculator()
        calc_variable.power(n1, n2)
    else:
        print("Invalid Choice!")
        
    calc_variable.display_result()


def main():
    print("-----Simple Calculator-----")

    while True:
        print("\n Choose the number between(1-6) for operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (Scientific Calculator)")
        print("6. Exit")

        choice = checking_valid_choice()

        if choice == 6:
            print("Exiting the program. Thank you!")
            sys.exit()
        else:
            user_Choice(choice)
