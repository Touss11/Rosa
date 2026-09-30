from src.calculator import calculate_recommended_time

import streamlit as st

from src.constants import ZONES, TIME_BLOCKS


def main():
    st.set_page_config(page_title="Promised Time Calculator")

    st.title("Promised Time Calculator")

    promised_time_range = st.slider(
        "Promised-time range (minutes)",
        min_value=5,
        max_value=120,
        value=(30, 60),
        step=5,
    )

    selected_zone = st.selectbox("Select a zone", ZONES)
    selected_time_block = st.selectbox("Select a time block", TIME_BLOCKS)

    profit_margin = st.number_input(
        "Profit margin per order",
        min_value=0.0,
        value=0.20,
        step=0.01,
        format="%.2f",
    )

    estimated_churn = st.number_input(
        "Estimated churn per late order",
        min_value=0.0,
        value=0.10,
        step=0.01,
        format="%.2f",
    )

    refund_cost = st.number_input(
        "Refund cost per late order",
        min_value=0.0,
        value=5.00,
        step=0.50,
        format="%.2f",
    )

    if st.button("Calculate Recommended Promised Time"):
        recommended_time = calculate_recommended_time(
            promised_time_range=promised_time_range,
            profit_margin=profit_margin,
            estimated_churn=estimated_churn,
            refund_cost=refund_cost,
            zone=selected_zone,
            time_block=selected_time_block,
        )

        st.success(
            f"Recommended promised time: "
            f"{recommended_time:.0f} minutes"
        )


if __name__ == "__main__":
    main()