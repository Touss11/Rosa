def calculate_recommended_time(
    promised_time_range,
    zone,
    time_block,
    profit_margin,
    estimated_churn,
    refund_cost,
):
    min_time, max_time = promised_time_range

    # Temporary calculation
    return (min_time + max_time) / 2