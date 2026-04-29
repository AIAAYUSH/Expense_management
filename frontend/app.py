import streamlit as st
from streamlit_option_menu import option_menu
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_months import analytics_months_tab
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF4B4B;
        color:white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# Expense Tracking System")


# Nice horizontal menu
selected = option_menu(
    None, ["Add/Update", "Analytics", "Analytics by months"],
    icons=['pencil-fill', 'bar-chart', 'calendar'],
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0E1117"},
        "icon": {"color": "#FF4B4B", "font-size": "18px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px"},
        "nav-link-selected": {"background-color": "#262730"},
    }
)

# Render the selected tab
if selected == "Add/Update":
    add_update_tab()
elif selected == "Analytics":
    analytics_tab()
elif selected == "Analytics by months":
    analytics_months_tab()
