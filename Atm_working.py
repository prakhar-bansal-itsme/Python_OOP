class Atm:

    # static variable, double underscore for private
    __counter = 1

    # Constructor
    def __init__(self):

        # Nothing in python is truly private

        # __ double underscore is used before any variable name to make it private
        # unlike java or c++ there is no private keyword
        # similarly we can use __ before a method name
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        self.menu()

    def get_counter():
        return Atm.__counter
    
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Type not valid, Please enter an Integer")

    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("PIN changed")
    
    def menu(self):
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit
                            """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")
            
    def create_pin(self):
        self.__pin = input("Enter your PIN")
        print("PIN set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance + amount
            print("Deposit successful")
        else:
            print("Invalid PIN")
        self.menu()
        
        
    def withdraw(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("Withdraw successful")
            else:
                print("Insufficient Fund")
        else:
            print("Invalid PIN")
        self.menu()
        

    def check_balance(self):
        temp = input("Enter the PIN")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid PIN")
        self.menu()

atm = Atm() 