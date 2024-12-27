class ATM():
    def __init__(self, balance):
        self.balance = balance

    def showProgramOptions(self):
        options = {
            "1" : "Check Balance",
            "2" : "Deposit",
            "3" : "Withdraw",
            "4" : "Exit"
        }
        
        for i in options:
            print(f"{i}. {options[i]} ")

        

    def showBalance(self):
        print(f"Your current balance is: ${self.balance}")


    def main(self):
        print("\nWelcome to the ATM!")
        self.showProgramOptions()
        self.showBalance()
    
     
    
ATM = ATM(0)
ATM.main()
