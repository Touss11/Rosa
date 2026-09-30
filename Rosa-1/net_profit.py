from data import ZONES, TIME_BLOCKS
from costs import COSTS, get_single_numeric_input
from promises import get_numeric_list_from_user
from delivery_times import delivery_times
from net_profit import calculate_net_profit

def main():
    print("Welcome to the Profitability Analysis Tool")
    
    # User selects a zone and time block
    zone = input(f"Select a zone from the following options: {', '.join(ZONES)}: ")
    time_block = input(f"Select a time block from the following options: {', '.join(TIME_BLOCKS)}: ")
    
    # User adjusts profit margin, churn per late order, and refund cost per late order
    profit_margin = get_single_numeric_input("Enter the profit margin: ")
    churn_per_late_order = get_single_numeric_input("Enter the churn cost per late order: ")
    refund_cost_per_late_order = get_single_numeric_input("Enter the refund cost per late order: ")
    
    # User selects a range of promise times
    promise_times = get_numeric_list_from_user("Enter the range of promise times you want to study (comma-separated): ")
    
    results = []
    
    for p in promise_times:
        times = delivery_times(zone, time_block, p)
        net_profit = calculate_net_profit(times, p, profit_margin, churn_per_late_order, refund_cost_per_late_order)
        results.append({"zone": zone, "time_block": time_block, "promise": p, "net_profit": net_profit})
    
    sorted_results = sorted(results, key=lambda x: x['net_profit'], reverse=True)
    
    print("Most profitable promise options:")
    for i, item in enumerate(sorted_results):
        print(f"{i+1}. Zone: {item['zone']}, Time Block: {item['time_block']}, Promise: {item['promise']}, Net Profit: {item['net_profit']}")

if __name__ == "__main__":
    main()