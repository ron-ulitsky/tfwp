import streamlit as st
import pandas as pd

# Load processed data
# You can change this path if needed
DATA_PATH = 'output/processed_output.xlsx'

def main():
    st.title('Canadian Temporary Work Permits by Occupation and Month')
    st.markdown('This dashboard shows the number of temporary work permits granted, broken down by occupation and month.')
    st.markdown('Data Source: [Government of Canada Open Data](https://open.canada.ca/data/en/dataset/360024f2-17e9-4558-bfc1-3616485d65b9)')

    # Load data
    df = pd.read_excel(DATA_PATH, index_col=0)

    # Show raw data
    st.subheader('Raw Data Table')
    st.dataframe(df)

    # Occupation filter
    occupations = df.index.tolist()
    selected_occupations = st.multiselect('Select Occupations', occupations, default=occupations[:10])
    filtered_df = df.loc[selected_occupations]

    # Month filter
    months = df.columns.tolist()
    selected_months = st.multiselect('Select Months', months, default=months)
    filtered_df = filtered_df[selected_months]

    # Show filtered table
    st.subheader('Filtered Data')
    st.dataframe(filtered_df)

    # Show a chart (sum by month)
    st.subheader('Total Permits by Month')
    st.bar_chart(filtered_df.sum(axis=0))

    # Show a chart (sum by occupation)
    st.subheader('Total Permits by Occupation')
    st.bar_chart(filtered_df.sum(axis=1))

if __name__ == '__main__':
    main()
