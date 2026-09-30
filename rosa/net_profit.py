from streamlit import st
from costs import COSTS

def calculate_net_profit(promise_range, costs, zone, time_block):
    # Example calculation logic for net profit
    refund = costs['refund']
    churn_orders = costs['churn_orders']
    margin = costs['margin']
    
    # Placeholder for actual profit calculation
    net_profit = (promise_range - (refund + churn_orders)) * margin
    return net_profit

st.title("Net Profit Calculator")

# User inputs for promise range, zone, and time block
promise_range = st.number_input("Set Promise Range:", min_value=0.0, value=100.0)
zone = st.selectbox("Select Zone:", ["Zone 1", "Zone 2", "Zone 3"])
time_block = st.selectbox("Select Time Block:", ["Morning", "Afternoon", "Evening"])

# Display current costs
st.write("Current Costs:", COSTS)

# Adjust costs
new_refund = st.number_input("Enter new refund value:", value=COSTS['refund'])
new_churn_orders = st.number_input("Enter new churn_orders value:", value=COSTS['churn_orders'])
new_margin = st.number_input("Enter new margin value:", value=COSTS['margin'])

# Update the COSTS dictionary
COSTS['refund'] = new_refund
COSTS['churn_orders'] = new_churn_orders
COSTS['margin'] = new_margin

# Calculate net profit
net_profit = calculate_net_profit(promise_range, COSTS, zone, time_block)

# Display the calculated net profit
st.write("Calculated Net Profit:", net_profit)