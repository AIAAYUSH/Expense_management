import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import altair as alt

API_URL = "http://localhost:8000"

def analytics_tab():
    st.title("Expense Analytics")

    # Date inputs
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload).json()

        # Prepare DataFrame
        data = {
            "Category": list(response.keys()),
            "Total": [response[cat]["total"] for cat in response],
            "Percentage": [response[cat]["percentage"] for cat in response]
        }

        df = pd.DataFrame(data)
        df_sorted = df.sort_values(by="Percentage", ascending=False)

        # Quick stats
        total_expense = df_sorted["Total"].sum()
        max_expense = df_sorted["Total"].max()
        avg_expense = df_sorted["Total"].mean()

        stat_col1, stat_col2, stat_col3 = st.columns(3)
        stat_col1.metric("Total Expense", f" ₹{total_expense:.2f}")
        stat_col2.metric("Max Expense", f" ₹{max_expense:.2f}")
        stat_col3.metric("Average Expense", f" ₹{avg_expense:.2f}")

        # Altair bar chart
        chart = alt.Chart(df_sorted).mark_bar().encode(
            x=alt.X('Category', sort='-y'),
            y='Percentage',
            color=alt.Color('Category', legend=None)
        ).properties(height=300)

        st.subheader("Expense Breakdown by Category")
        st.altair_chart(chart, use_container_width=True)

        # Scrollable dataframe
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)
        st.subheader("Detailed Table")
        st.dataframe(df_sorted, use_container_width=True)
