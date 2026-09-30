from data import ZONES, TIME_BLOCKS, COSTS
from costs import get_single_numeric_input
from promises import get_numeric_list_from_user
from delivery_times import delivery_times

results = []
zone = input("Enter the zone you want to study: ")
time_block = input("Enter the time_block you want to study: ")

for p in get_numeric_list_from_user("Enter the promise values you want to study (comma-separated): "):
  times = delivery_times(zone, time_block, p)
  late_deliveries_count = (times > p).sum()
  total_deliveries_count = len(times)
  on_time_deliveries_count = total_deliveries_count - late_deliveries_count
  costs_per_late_order = COSTS['refund'] + COSTS['churn_orders']
  net_profit = ((on_time_deliveries_count)*COSTS['margin']) - (late_deliveries_count*costs_per_late_order)
  results.append({"zone": zone, "time_block": time_block, "promise": p, "net_profit": net_profit})

sorted_results = sorted(results, key=lambda x: x['net_profit'], reverse=True)

print("Pairs ranking by net_profit :")
for i, item in enumerate(sorted_results):
  print(f"{i+1}. Zone: {item['zone']}, Time Block: {item['time_block']}, Promise: {item['promise']}, net_profit : {item['net_profit']}")