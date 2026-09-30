from data import ZONES, TIME_BLOCKS
from costs import COSTS, get_single_numeric_input
from promises import get_numeric_list_from_user
from delivery_times import delivery_times

def main():
    print("Welcome to the Profitability Analysis Tool")
    
    # User selects zone and time block
    zone = input(f"Select a zone from the following options: {', '.join(ZONES)}: ")
    time_block = input(f"Select a time block from the following options: {', '.join(TIME_BLOCKS)}: ")
    
    # User adjusts profit margin, churn cost, and refund cost
    profit_margin = get_single_numeric_input("Enter the profit margin: ", default=COSTS['margin'])
    churn_cost = get_single_numeric_input("Enter the churn cost per late order: ", default=COSTS['churn_orders'])
    refund_cost = get_single_numeric_input("Enter the refund cost per late order: ", default=COSTS['refund'])
    
    # User selects a range of promise times
    promise_range = get_numeric_list_from_user("Enter the range of promise times you want to study (comma-separated): ")
    
    results = []
    
    for p in promise_range:
        times = delivery_times(zone, time_block, p)
        late_deliveries_count = (times > p).sum()
        total_deliveries_count = len(times)
        on_time_deliveries_count = total_deliveries_count - late_deliveries_count
        
        net_profit = (on_time_deliveries_count * profit_margin) - (late_deliveries_count * (churn_cost + refund_cost))
        results.append({"zone": zone, "time_block": time_block, "promise": p, "net_profit": net_profit})
    
    sorted_results = sorted(results, key=lambda x: x['net_profit'], reverse=True)
    
    print("Most profitable promise options:")
    for i, item in enumerate(sorted_results):
        print(f"{i+1}. Zone: {item['zone']}, Time Block: {item['time_block']}, Promise: {item['promise']}, Net Profit: {item['net_profit']}")

if __name__ == "__main__":
    main()