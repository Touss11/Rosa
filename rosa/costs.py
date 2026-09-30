# filepath: /rosa/rosa/costs.py
COSTS = {
    'refund': 0.0,
    'churn_orders': 0.0,
    'margin': 0.0
}

def update_costs(refund, churn_orders, margin):
    COSTS['refund'] = refund
    COSTS['churn_orders'] = churn_orders
    COSTS['margin'] = margin

def get_costs():
    return COSTS.copy()