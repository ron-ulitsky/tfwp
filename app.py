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


    # Hideable filters using expander
    with st.expander('Show/Hide Filters', expanded=False):
        occupations = df.index.tolist()
        selected_occupations = st.multiselect('Select Occupations', occupations, default=occupations[:10])
        months = df.columns.tolist()
        # Use a select_slider for months (range selection)
        selected_month_range = st.select_slider(
            'Select Month Range',
            options=months,
            value=(months[0], months[-1])
        )
        # Get the indices for the selected range
        start_idx = months.index(selected_month_range[0])
        end_idx = months.index(selected_month_range[1])
        selected_months = months[start_idx:end_idx+1]

    filtered_df = df.loc[selected_occupations][selected_months]

    # Pie chart of permits by occupation (using Plotly)
    import plotly.express as px
    st.subheader('Permits Distribution by Occupation')
    occupation_totals = filtered_df.sum(axis=1)
    pie_df = pd.DataFrame({
        'Occupation': occupation_totals.index,
        'Permits': occupation_totals.values
    })
    fig = px.pie(pie_df, names='Occupation', values='Permits')
    st.plotly_chart(fig, use_container_width=True)

    # Show a chart (sum by month)
    st.subheader('Total Permits by Month')
    # Ensure months are sorted chronologically
    month_totals = filtered_df.sum(axis=0).reindex(selected_months)

    import plotly.graph_objects as go
    fig_month = go.Figure(go.Bar(x=month_totals.index, y=month_totals.values))
    fig_month.update_layout(xaxis_title='Month', yaxis_title='Total Permits')
    st.plotly_chart(fig_month, use_container_width=True)

    # Show a chart (sum by occupation)
    st.subheader('Total Permits by Occupation')
    st.bar_chart(occupation_totals)

    # Show filtered table
    st.subheader('Filtered Data')
    st.dataframe(filtered_df)

    # Show raw data at the end
    st.subheader('Raw Data Table')
    st.dataframe(df)

if __name__ == '__main__':
    main()
