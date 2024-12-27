class ATM():

    def __init__(self, balance):
        self.balance = balance

    def show_program_options(self):
        options = ("Check Balance", "Deposit", "Withdraw", "Exit")
        for i, value in enumerate(options, start=1):
            print(f"{i}. {value}")


    def show_balance(self):
        print(f"\nYour current balance is: ${self.balance}")


    def make_deposit(self):
        while True:
            try:
                deposit_amount = float(input("\nEnter the amount to deposit: $").strip())
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")

                else:
                    self.balance = deposit_amount
                    print(f"Sucessfuly deposited ${deposit_amount}.")
                    return
            except ValueError:
                print("Please enter a valid number.")


    def withdraw_money(self):
        if self.balance > 0:
            
            while True:
                try:
                    withdrawal_amount = float(input("\nEnter the amount to withdraw: $").strip())
                    if withdrawal_amount <= 0:
                        print("Witdrawal amount must be positive.")

                    elif withdrawal_amount > self.balance:
                        print("Insufficient funds.")

                    else:
                        self.balance -= withdrawal_amount
                        print(f"Sucessfuly withdrew ${withdrawal_amount}.")
                        return
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print(f"Your balance is {self.balance}. There is no money to withdraw")

    def exit_program(self):
        print("Exiting program. Goodbye!")
        exit()

    def program_operations(self):
        return {
        "1": self.show_balance, 
        "2": self.make_deposit,
        "3": self.withdraw_money,
        "4": self.exit_program
        }

        

    def get_user_option(self):
        while True:
            try:
                chosen_option = int(input("Please choose an option: ").strip())
                if chosen_option < 1 or chosen_option > 4:
                    print("You have only 4 operations.")
                else:
                    return chosen_option
            except ValueError:
                print("Type a number for the corresponding operation")


    def main(self):
        
        while True:
            print("\nWelcome to the ATM!")
            self.show_program_options()
            option = self.get_user_option()
            operation = self.program_operations().get(str(option))
            if operation:
                operation()
            else:
                print("Invalid option. PLease try again.")
    
     
    
ATM = ATM(0)
ATM.main()
