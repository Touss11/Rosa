from streamlit import st
from src.calculator import calculate_recommended_time
from src.constants import ZONES, TIME_BLOCKS

def main():
    st.title("Promised Time Calculator")

    promised_time_range = st.slider("Select the range of promised times (minutes)", 0, 120, (30, 60))
    selected_zone = st.selectbox("Select a zone", ZONES)
    selected_time_block = st.selectbox("Select a time block", TIME_BLOCKS)
    profit_margin = st.number_input("Adjust profit margin per order", min_value=0.0, value=0.2, format="%.2f")
    estimated_churn = st.number_input("Estimated churn per late order", min_value=0.0, value=0.1, format="%.2f")
    refund_cost = st.number_input("Refund cost per late order", min_value=0.0, value=5.0, format="%.2f")

    if st.button("Calculate Recommended Promised Time"):
        recommended_time = calculate_recommended_time(promised_time_range, profit_margin, estimated_churn, refund_cost)
        st.success(f"The recommended promised time is: {recommended_time:.2f} minutes")

if __name__ == "__main__":
    main()