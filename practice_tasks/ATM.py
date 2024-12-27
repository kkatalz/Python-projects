class ATM():
    def __init__(self, balance):
        self.balance = balance

    def show_program_options(self):
        options = {
            "1" : "Check Balance",
            "2" : "Deposit",
            "3" : "Withdraw",
            "4" : "Exit"
        }
        
        for i in options:
            print(f"{i}. {options[i]} ")

        

    def show_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def make_deposit(self):
        while True:
            try:
                deposit_amount = float(input("\nEnter the amount to deposit: ").strip())
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")

                else:
                    self.balance = deposit_amount
                    print(f"Sucessfuly deposited ${deposit_amount}.")
                    return
            except ValueError:
                print("Please enter a valid number.")




    def main(self):
        
        print("\nWelcome to the ATM!")
        self.show_program_options()

        # chosen_option = input("Please choose an option: ").strip()
        
        self.make_deposit()
        print(self.balance)
    
     
    
ATM = ATM(0)
ATM.main()
