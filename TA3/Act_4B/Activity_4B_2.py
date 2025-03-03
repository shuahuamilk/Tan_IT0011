import csv

exchange_rates = {}

with open("currency.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  #skip header row
    for row in reader:
        if len(row) == 3:
            code, _, rate = row  #just use code and rate
            exchange_rates[code] = float(rate)

# user input
usd_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency do you want to have? ").upper()

#currency converion
if target_currency in exchange_rates:
    converted_amount = usd_amount * exchange_rates[target_currency]
    print(f"\nDollar: {usd_amount:.2f} USD")
    print(f"{target_currency}: {converted_amount:.6f}")
else:
    print(f"Error: Currency '{target_currency}' not found in exchange rates.")
