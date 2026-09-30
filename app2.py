import streamlit as st
import pandas as pd

from data import ZONES, TIME_BLOCKS
from delivery_times import delivery_times


st.set_page_config(page_title="Rosa Promise Optimizer", page_icon="🚚")

st.title("Rosa Promise Optimizer")
st.write("Find the most profitable promised delivery time.")


def calculate_results(zone, time_block, promises, margin, churn, refund):
    results = []

    for promise in promises:
        times = delivery_times(zone, time_block, promise)

        late_count = int((times > promise).sum())
        total_count = len(times)
        on_time_count = total_count - late_count

        net_profit = (
            on_time_count * margin
            - late_count * (refund + churn)
        )

        results.append(
            {
                "Promise (minutes)": promise,
                "On-time orders": on_time_count,
                "Late orders": late_count,
                "Net profit ($)": round(net_profit, 2),
            }
        )

    return pd.DataFrame(results).sort_values(
        by="Net profit ($)",
        ascending=False,
    )


# Promise range, in five-minute steps
promise_range = st.slider(
    "Promise time range (minutes)",
    min_value=5,
    max_value=180,
    value=(30, 60),
    step=5,
)

zone = st.selectbox("Zone", list(ZONES))
time_block = st.selectbox("Time block", list(TIME_BLOCKS))

margin = st.number_input(
    "Profit margin per order ($)",
    min_value=0.0,
    value=9.0,
    step=0.10,
    format="%.2f",
)

churn = st.number_input(
    "Estimated churn per late order ($)",
    min_value=0.0,
    value=1.80,
    step=0.10,
    format="%.2f",
)

refund = st.number_input(
    "Refund cost per late order ($)",
    min_value=0.0,
    value=10.0,
    step=0.10,
    format="%.2f",
)

if st.button("Calculate most profitable promise", type="primary"):
    start, end = promise_range
    promises = list(range(start, end + 1, 5))

    results = calculate_results(
        zone=zone,
        time_block=time_block,
        promises=promises,
        margin=margin,
        churn=churn,
        refund=refund,
    )

    if results.empty:
        st.warning("No results were calculated.")
    else:
        best = results.iloc[0]

        st.success(
            f"Recommended promise: **{int(best['Promise (minutes)'])} minutes** "
            f"with a net profit of **${best['Net profit ($)']:.2f}**"
        )

        st.subheader("Promise options ranked by net profit")
        st.dataframe(results, hide_index=True, use_container_width=True)