TAX_RATE = 0.06

def display_title() -> None:
    print("Sales Tax Calculator")

def get_items_total() -> float:
    total = 0.0
    while True:
        cost = float(input("Cost of item: "))
        if cost == 0:
            break
        total += cost
    return total

def process_all() -> None:
    display_title()
    while True:
        print("ENTER ITEMS (ENTER 0 TO END)")
        total = get_items_total()
        sales_tax = total * TAX_RATE
        total_after_tax = total + sales_tax
        print(f"Total: {round(total, 2)}")
        print(f"Sales tax: {round(sales_tax, 2)}")
        print(f"Total after tax: {round(total_after_tax, 2)}")
        again = input("Again? (y/n): ")
        if again.lower() == "n":
            print("Thanks, bye!")
            break
        print()

process_all()