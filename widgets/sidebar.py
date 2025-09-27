import streamlit as st
from config import DEFAULT_MONTHS

def sidebar_filters(df):
    st.sidebar.header('Filters')
    occupations = df.index.tolist()

    months = df.columns.tolist()
    # Default to last n months
    if len(months) >= DEFAULT_MONTHS:
        default_start = months[-DEFAULT_MONTHS]
        default_end = months[-1]
    else:
        default_start = months[0]
        default_end = months[-1]
    selected_month_range = st.sidebar.select_slider(
        'Select Month Range',
        options=months,
        value=(default_start, default_end)
    )
    start_idx = months.index(selected_month_range[0])
    end_idx = months.index(selected_month_range[1])
    selected_months = months[start_idx:end_idx+1]

    selected_occupations = st.sidebar.multiselect('Select Occupations', occupations, default=occupations)

    return selected_months, selected_occupations