
def money_number():
    while True:
        try:
            money_amount = float(input("Enter the amount of money: "))
            if money_amount <= 0:
                raise ValueError
            return money_amount
        except ValueError:
            print("Invalid input!")
            continue


def get_currency(given_currency):
    currencies = ("usd", "eur", "cad")
    while True:
        currency = input(f"{given_currency} currency (USD/EUR/CAD): ").lower()
        if currency not in currencies:
            print("Invalid input!")
            continue
        return currency

def convert_currency(money_amount, source_currency, target_currency):
    exchange_rates = {
        'usd': {'eur': 0.95, 'cad': 1.42},
        'eur': {'usd': 1.05, 'cad': 1.49},
        'cad': {'usd': 0.71, 'eur': 0.67}
    }
    
    if source_currency == target_currency:
        return money_amount

    return money_amount * exchange_rates[source_currency][target_currency]
    


def currency_converter():
    money_amount = money_number()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted_amount = convert_currency(money_amount, source_currency, target_currency)

    print(f"{money_amount} {source_currency.upper()} is {round(converted_amount,2)} {target_currency.upper()}")
   

def convert_again():
    while True:
        user_input = input("Do you want to convert again? (y/n): ").lower()
        if user_input == "y":
            currency_converter()
            continue
        else:
            print("Thanks for using the currency converter!")
            break

currency_converter()
convert_again()