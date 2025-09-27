import streamlit as st

def sidebar_filters(df):
    st.sidebar.header('Filters')
    occupations = df.index.tolist()

    months = df.columns.tolist()
    selected_month_range = st.sidebar.select_slider(
        'Select Month Range',
        options=months,
        value=(months[0], months[-1])
    )
    start_idx = months.index(selected_month_range[0])
    end_idx = months.index(selected_month_range[1])
    selected_months = months[start_idx:end_idx+1]

    selected_occupations = st.sidebar.multiselect('Select Occupations', occupations, default=occupations)

    return selected_months, selected_occupations