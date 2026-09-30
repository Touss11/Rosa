import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from net_profit2 import calculate_net_profits
from src.constants import ZONES, TIME_BLOCKS


st.set_page_config(page_title="Rosa Promised Time Optimizer")


def main():
    st.title("Rosa Promised Time Optimizer")

    promised_time_range = st.slider(
        "Range of promised times (minutes)",
        min_value=5,
        max_value=120,
        value=(30, 60),
        step=5,
    )

    selected_zone = st.selectbox("Zone", ZONES)
    selected_time_block = st.selectbox("Time block", TIME_BLOCKS)

    profit_margin = st.number_input(
        "Profit margin per order ($)",
        min_value=0.0,
        value=9.0,
        step=0.10,
        format="%.2f",
    )

    estimated_churn = st.number_input(
        "Churn cost per late order ($)",
        min_value=0.0,
        value=1.8,
        step=0.10,
        format="%.2f",
    )

    refund_cost = st.number_input(
        "Refund cost per late order ($)",
        min_value=0.0,
        value=10.0,
        step=0.10,
        format="%.2f",
    )

    if st.button("Find the most profitable promise", type="primary"):
        promise_values = range(
            promised_time_range[0],
            promised_time_range[1] + 1,
            5,
        )

        results = calculate_net_profits(
            zone=selected_zone,
            time_block=selected_time_block,
            promise_values=promise_values,
            profit_margin=profit_margin,
            estimated_churn=estimated_churn,
            refund_cost=refund_cost,
        )

        best_result = results[0]

        st.success(
            f"Most profitable promise: "
            f"{best_result['promise']} minutes "
            f"with net profit of "
            f"${best_result['net_profit']:.2f}"
        )

        st.dataframe(results, use_container_width=True)


if __name__ == "__main__":
    main()