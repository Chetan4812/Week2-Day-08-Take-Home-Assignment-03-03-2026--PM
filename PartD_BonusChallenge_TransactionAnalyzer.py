transactions = []

total_credits = 0
total_debits = 0
transaction_count = 0
highest_transaction = 0

categories = {}

print("=== Paytm Mini Analytics Dashboard ===")

# ===============================
# TODO 1: While loop - keep taking transactions until 'done'
# ===============================
while True:
    user_input = input("\nEnter transaction amount (or type 'done'): ")

    if user_input.lower() == "done":
        break

    try:
        amount = float(user_input)
    except ValueError:
        print("Invalid amount. Try again.")
        continue

    txn_type = input("Enter type (credit/debit): ").lower()

    if txn_type not in ["credit", "debit"]:
        print("Invalid type. Try again.")
        continue

    # TODO 2: Store amount and type
    transaction = {
        "amount": amount,
        "type": txn_type
    }

    # Bonus: Category input (only for debit)
    if txn_type == "debit":
        category = input("Enter category (food/travel/bills/other): ").lower()
        transaction["category"] = category

        # Update category tracking
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    transactions.append(transaction)
    transaction_count += 1

    # TODO 3: Flag high-value transactions (> 10000)
    if amount > 10000:
        print("⚠ High-value transaction detected!")

    # Track totals
    if txn_type == "credit":
        total_credits += amount
    else:
        total_debits += amount

    # Track highest transaction
    if amount > highest_transaction:
        highest_transaction = amount


# ===============================
# TODO 4: Calculate summary stats
# ===============================
net_balance = total_credits - total_debits

if transaction_count > 0:
    average_amount = sum(txn["amount"] for txn in transactions) / transaction_count
else:
    average_amount = 0


# ===============================
# TODO 5: Print bar chart of last 10 transactions
# ===============================
print("\n=== Last 10 Transactions Bar Chart ===")
last_10 = transactions[-10:]

for txn in last_10:   # FOR LOOP USED HERE
    stars = int(txn["amount"] // 1000)
    print(f"{txn['type'].upper()} ₹{txn['amount']} | {'*' * stars}")


# ===============================
# TODO 6: Print Summary
# ===============================
print("\n=== SUMMARY ===")
print("Total transactions:", transaction_count)
print("Total Credits: ₹", total_credits)
print("Total Debits: ₹", total_debits)
print("Net Balance: ₹", net_balance)
print("Highest Transaction: ₹", highest_transaction)
print("Average Transaction Amount: ₹", round(average_amount, 2))


# ===============================
# Bonus: Spending Breakdown
# ===============================
if categories:
    print("\n=== Spending Breakdown by Category ===")
    for category, amount in categories.items():
        print(f"{category.capitalize()}: ₹{amount}")