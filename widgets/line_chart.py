import streamlit as st
import pandas as pd
import plotly.express as px
from maps.noc import noc_broad_categories

def line_chart_by_broad_category_over_time(filtered_df):
    st.subheader('Permits Issued by NOC Broad Category Over Time')
    # Get broad category for each occupation
    def get_broad_category(noc):
        return str(noc)[0]
    # Aggregate by broad category and month
    occupation_totals = filtered_df.copy()
    occupation_totals['Broad Category'] = occupation_totals.index.map(get_broad_category)
    # Sum by broad category and month
    grouped = occupation_totals.groupby('Broad Category').sum()
    # Transpose for plotting (rows: months, columns: broad categories)
    grouped = grouped.T
    # Rename columns to category names
    grouped.columns = [noc_broad_categories.get(cat, f'NOC Category {cat}') for cat in grouped.columns]
    # Plot
    fig = px.line(grouped, x=grouped.index, y=grouped.columns, labels={'value': 'Permits', 'variable': 'Broad Category', 'index': 'Month'})
    fig.update_layout(legend_orientation="h", legend_y=-0.2)
    st.plotly_chart(fig, use_container_width=True)
