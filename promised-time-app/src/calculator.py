def calculate_recommended_time(promised_time_range, profit_margin, estimated_churn, refund_cost):
    min_time, max_time = promised_time_range
    recommended_time = (min_time + max_time) / 2  # Simple average for demonstration
    return recommended_time