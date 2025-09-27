import streamlit as st

def filtered_table(filtered_df):
    # Show filtered table
    st.subheader('Filtered Data')
    st.dataframe(filtered_df)