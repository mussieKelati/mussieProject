from exchange import CurrencyConverter

def menu():
    print("Currency Conversion Menu:")
    print("1. USD to EUR")
    print("2. EUR to USD")
    print("3. SHL to USD")
    print("4. USD to SHL")

def main():
    menu()
    choice = input("Choose a conversion pair (1,2,3,4,): ")

    amount = (input("Enter the amount to convert: "))

    if choice == '1':
        converted_amount = CurrencyConverter.usd_to_eur(amount)
        print(f"{amount} USD is {converted_amount} EUR")
    elif choice == '2':
        converted_amount = CurrencyConverter.eur_to_usd(amount)
        print(f"{amount} EUR is {converted_amount} USD")
    elif choice == '3':
        converted_amount = CurrencyConverter.shl_to_usd(amount)
        print(f"{amount} SHL is {converted_amount} USD")
    elif choice == '4':
        converted_amount = CurrencyConverter.usd_to_shl(amount)
        print(f"{amount} USD is {converted_amount} SHL")
    else:
        print("Invalid choice Please choose from 1 to 4.")

main()
