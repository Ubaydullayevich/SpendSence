import csv

def run_categorizer():
    print("\n=== Categorization Agent ===")

    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            description = row["description"].lower()

            if "coffee" in description or "restaurant" in description or "starbucks" in description or "mcdonalds" in description:
                category = "Food"
            elif "taxi" in description or "uber" in description or "bus" in description:
                category = "Transport"
            elif "netflix" in description or "spotify" in description or "youtube" in description:
                category = "Subscription"
            elif "rent" in description:
                category = "Housing"
            elif "shopping" in description or "electronics" in description:
                category = "Shopping"
            elif "cinema" in description:
                category = "Entertainment"
            elif "groceries" in description:
                category = "Groceries"
            else:
                category = "Other"

            print(f"{row['description']} -> {category}")
