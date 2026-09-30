COSTS = {
    'margin': 0.2,  # Default profit margin
    'churn_orders': 5.0,  # Default churn cost per late order
    'refund': 10.0  # Default refund cost per late order
}

def get_costs():
    return COSTS

def set_costs(margin=None, churn_orders=None, refund=None):
    if margin is not None:
        COSTS['margin'] = margin
    if churn_orders is not None:
        COSTS['churn_orders'] = churn_orders
    if refund is not None:
        COSTS['refund'] = refund