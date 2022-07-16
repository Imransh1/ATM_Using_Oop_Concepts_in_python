class Atm:
    def __init__(self):
        #constructor
        self.__pin = 0
        self.__balance = 0
        self.__menu()
        # using double underscores before attribute/method name to encapsulate/hide data from objects
        # and avoid manipulation. Note - Data is hidden from objects but still accessible using '_Atm__pin' or '_Atm__balance/menu'
        # So it is not private. 

    def __menu(self):
        #ATM Menu
        user_input = int(input("""
        Hello. How would you like to proceed?
        1. Press 1 to Generate New Pin
        2. Press 2 to Change pin
        3. Press 3 to Check Balance
        4. Press 4 to Withdraw
        5. Press 5 to Deposit
        6. Press 6 to Exit
        """))
        if user_input == 1:
            self.generate_pin()
        elif user_input == 2:
            self.change_pin()
        elif user_input == 3:
            self.check_balance()
        elif user_input == 4:
            self.withdraw()
        elif user_input == 5:
            self.deposit()
        elif user_input == 6:
            print('\nThank you for using ATM')
            exit()
        else:
            while True:
                print("Please choose correct option! \n" )
                self.__menu()
    def generate_pin(self):
        # Generating New pin
        if self.__pin == 0:
            new_pin = int(input('Please enter new 4 digit Pin: '))
            con_pin = int(input('Please confirm new 4 digit Pin: '))
            if new_pin == con_pin:
                self.__pin = con_pin
                print('Pin set successfully')
                self.__menu()
            else:
                print('Pin does not match. Try again!')
                self.__menu()
        else:
            print('Pin is already generated. Select change pin if you want to change it.')
            self.__menu()
    
    def change_pin(self):
        # changing current pin if pin is set.
        if self.__pin == 0:
            print('Please generate pin first. Select generate new pin option from menu.')
            self.__menu()
        else:
            con_old_pin = int(input('Please confirm old Pin: '))
            if con_old_pin == self.__pin:
                new_pin = int(input('Please enter new 4 digit Pin: '))
                con_pin = int(input('Please confirm new 4 digit Pin: '))
                if new_pin == con_pin:
                    self.__pin = con_pin
                    print('Pin set successfully')
                    self.__menu()
                else:
                    print('Both pin does not match.')
                    self.__menu()
            else:
                print('Sorry, Wrong Pin')
                self.__menu()
    
    def check_balance(self):
        # checking current balance after confirming pin
        if self.__pin == 0:
            print('Please generate pin first. Select generate new pin option from menu.')
            self.__menu()
        else:
            pin = int(input('Please enter your pin: '))
            if pin == self.__pin:
                print(f"Your current balance is: {self.__balance}")
                self.__menu()
            else:
                print('Sorry, wrong pin! ')
                self.__menu()
    def withdraw(self):
        # withdraw cash after confirming pin and checking current_balance
        if self.__pin == 0:
            print('Please generate pin first. Select generate new pin option from menu.')
            self.__menu()
        else:
            pin = int(input('Please enter your pin: '))
            if pin == self.__pin:
                amount = int(input('Please enter amount to withdraw. Minimum amount is 100: '))
                if self.__balance >= amount and amount!= 0 and amount %100 == 0:
                    self.__balance -= amount
                    print('Withdrawal Successful! Take your cash.')
                    self.__menu()
                elif amount< 100:
                    print('Minimum Withdrawal Amount is 100')
                    self.__menu()
                elif amount %100 != 0:
                    print('Amount must be in multiple of 100s')
                    self.__menu()
                else:
                    print(f'Insufficient Balance: {self.__balance}')
                    self.__menu()
            else:
                print('Sorry, wrong pin! ')
                self.__menu()

    def deposit(self):
        # deposit after confirming pin and amount
        if self.__pin == 0:
            print('Please generate pin first. Select generate new pin option from menu.')
            self.__menu()
        else:
            pin = int(input('Please enter your pin: '))
            if pin == self.__pin:
                amount = int(input('Please enter amount to deposit: '))
                if amount == 0:
                    print('Amount must be greater than 0')
                    self.__menu()
                elif amount < 100:
                    print('Minimum deposit Amount is 100')
                    self.__menu()
                elif amount %100 != 0:
                    print('Amount must be in multiple of 100s')
                    self.__menu()
                else:
                    self.__balance += amount
                    print(f'Deposit Successful! Your current balance is: {self.__balance}')
                    self.__menu()
            else:
                print('Sorry, wrong pin!')
                self.__menu()


ATM_HDFC = Atm()
# object created using class Atm
# so object will behave like class itself
# no matter how many objects we create.