
import streamlit as st
import pandas as pd
import plotly.express as px
from maps.noc import noc_broad_categories

def pie_chart_by_broad_category(filtered_df, n_top=10):
    
    st.subheader('Permits Distribution by NOC Broad Category')
    with st.expander('What is a NOC Broad Category?', expanded=False):
        st.markdown("""
        NOC Broad Categories are the highest-level groupings in the National Occupational Classification (NOC) system, used by the Government of Canada to classify jobs by major field of work. Each broad category covers a wide range of related occupations.  

        [Learn more about NOC Concepts](https://noc.esdc.gc.ca/Home/ConceptsAndConventions)
        """)
    occupation_totals = filtered_df.sum(axis=1)
    def get_broad_category(noc):
        code = str(noc)[0]
        return code
    broad_category_totals = occupation_totals.groupby(get_broad_category).sum()
    pie_labels = [noc_broad_categories.get(cat, f'NOC Category {cat}') for cat in broad_category_totals.index]
    pie_data = list(broad_category_totals.values)
    pie_df = pd.DataFrame({
        'Broad Category': pie_labels,
        'Permits': pie_data
    })
    fig = px.pie(pie_df, names='Broad Category', values='Permits')
    fig.update_layout(legend_orientation="h", legend_y=-0.2)
    st.plotly_chart(fig, use_container_width=True)
