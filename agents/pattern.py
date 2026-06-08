import csv

def run_pattern():
    print("\n=== Pattern Agent ===")

    total = 0
    highest_amount = 0
    highest_item = ""
    subscriptions = []

    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])
            description = row["description"]

            total += amount

            if amount > highest_amount:
                highest_amount = amount
                highest_item = description

            if description.lower() in ["netflix", "spotify", "youtube premium"]:
                subscriptions.append(description)

    print(f"Total spending: ${total}")
    print(f"Highest transaction: {highest_item} (${highest_amount})")

    if subscriptions:
        print("Active subscriptions:", ", ".join(subscriptions))
