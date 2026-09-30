from data import ZONES, TIME_BLOCKS, COSTS
from costs import get_single_numeric_input
from promises import get_numeric_list_from_user
from delivery_times import delivery_times


def calculate_net_profits(
    zone,
    time_block,
    promise_values,
    profit_margin,
    estimated_churn,
    refund_cost,
):
    results = []
    late_order_cost = estimated_churn + refund_cost

    for promise in promise_values:
        times = delivery_times(zone, time_block, promise)

        late_deliveries = int((times > promise).sum())
        total_deliveries = len(times)
        on_time_deliveries = total_deliveries - late_deliveries

        net_profit = (
            on_time_deliveries * profit_margin
            - late_deliveries * late_order_cost
        )

        results.append(
            {
                "zone": zone,
                "time_block": time_block,
                "promise": promise,
                "net_profit": net_profit,
                "late_deliveries": late_deliveries,
                "on_time_deliveries": on_time_deliveries,
            }
        )

    return sorted(
        results,
        key=lambda result: result["net_profit"],
        reverse=True,
    )


def recommend_promised_time(
    zone,
    time_block,
    promise_values,
    profit_margin,
    estimated_churn,
    refund_cost,
):
    results = calculate_net_profits(
        zone,
        time_block,
        promise_values,
        profit_margin,
        estimated_churn,
        refund_cost,
    )

    if not results:
        raise ValueError("At least one promise value is required.")

    return results[0]