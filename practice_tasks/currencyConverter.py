
def money_number():
    while True:
        try:
            money_amount = float(input("Enter the amount of money: "))
            if money_amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input!")
            continue

    return money_amount

def currency_converter():

    currencies = ("usd", "eur", "cad")
    
    exchange_rates = {
        'usd': {'eur': 0.95, 'cad': 1.42},
        'eur': {'usd': 1.05, 'cad': 1.49},
        'cad': {'usd': 0.71, 'eur': 0.67}
    }
    money_amount = money_number()


    while True:
        source_currency = input("Source currency (USD/EUR/CAD): ").lower()
        if source_currency not in currencies:
            print("Invalid input!")
            continue
        break

    while True:
        target_currency = input("Target currency (USD/EUR/CAD): ").lower()
        if target_currency not in ("usd", "eur", "cad"):
            print("Invalid input!")
            continue
        break


    if source_currency == target_currency:
        converted_amount = money_amount    
    else:
        converted_amount = money_amount * exchange_rates[source_currency][target_currency]
    
    print(f"{money_amount} {source_currency.upper()} is {round(converted_amount,2)} {target_currency.upper()}")


def convert_again():
    user_input = ""
    while True:
        user_input = input("Do you want to convert again? (y/n): ").lower()
        if user_input == "y":
            currency_converter()
            continue
        else:
            print("Thanks for using the currency converter!")
            break

def main():
    convert_again()
    
currency_converter()
main()