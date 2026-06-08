import csv

def run_alert():
    print("\n=== Alert Agent ===")

    budget = 1000
    spent = 0

    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            spent += float(row["amount"])

    percent_used = (spent / budget) * 100

    print(f"Monthly budget: ${budget}")
    print(f"Spent so far: ${spent}")
    print(f"Budget used: {percent_used:.1f}%")

    if percent_used >= 80:
        print("⚠️ Alert: You have used more than 80% of your monthly budget.")
        print("Recommendation: Reduce shopping and restaurant spending this week.")
    else:
        print("✅ Budget status is healthy.")
