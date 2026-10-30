def greet_customer():
    print("Hello! Welcome to our Lemonade stand. How can I assist you today?")

greet_customer()

price_per_cup = float(input("Enter the price of the cup in dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

def calculate_total(price, cups):
    total = price * cups
    return total

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost: $", rounded_total)

amount_paid = float(input("Enter the amount paid by the customer in dollars: "))

def calculate_change(amount_paid, total_cost):
    change = amount_paid - total_cost
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups >= 5:
        return "Wow! big order! Thank you for your support!"
    else:
        return "Thank you for stopping by the stand"

closing_message = thank_you_message(cups_sold)

print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price per cup: $", round(price_per_cup, 2))
print("Cups sold: ", cups_sold)
print("Total cost: $", rounded_total)
print("Amount paid: $", round(amount_paid, 2))
print("Change due: $", rounded_change)
print(closing_message)
print("===================================")