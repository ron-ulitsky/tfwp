import streamlit as st

def raw_data_table(df):
    st.subheader('Raw Data Table')
    st.dataframe(df)