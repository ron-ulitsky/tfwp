import streamlit as st
import pandas as pd
import plotly.express as px
from maps.noc import noc_broad_categories

def stacked_bar_chart_by_broad_category_over_time(filtered_df):
    st.subheader('Stacked Bar Chart: Permits Issued by NOC Broad Category Over Time')
    # Get broad category for each occupation
    def get_broad_category(noc):
        return str(noc)[0]
    occupation_totals = filtered_df.copy()
    occupation_totals['Broad Category'] = occupation_totals.index.map(get_broad_category)
    # Sum by broad category and month
    grouped = occupation_totals.groupby('Broad Category').sum()
    grouped = grouped.T
    grouped.columns = [noc_broad_categories.get(cat, f'NOC Category {cat}') for cat in grouped.columns]
    # Melt for stacked bar chart
    stacked_df = grouped.reset_index().melt(id_vars='index', var_name='Broad Category', value_name='Permits')
    stacked_df.rename(columns={'index': 'Month'}, inplace=True)
    fig = px.bar(stacked_df, x='Month', y='Permits', color='Broad Category', barmode='stack')
    fig.update_layout(legend_orientation="h", legend_y=-0.2)
    st.plotly_chart(fig, use_container_width=True)
