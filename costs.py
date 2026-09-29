def get_single_numeric_input(prompt_message):
    while True:
        user_input = input(prompt_message)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

print("Current COSTS:", COSTS)

# Get new values from the user
new_refund = get_single_numeric_input("Enter new refund value: ")
new_churn_orders = get_single_numeric_input("Enter new churn_orders value: ")
new_margin = get_single_numeric_input("Enter new margin value: ")

# Update the COSTS dictionary
COSTS['refund'] = new_refund
COSTS['churn_orders'] = new_churn_orders
COSTS['margin'] = new_margin

print("Updated COSTS:", COSTS)
