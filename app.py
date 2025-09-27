import streamlit as st
import pandas as pd
from widgets.pie_chart import pie_chart_by_broad_category
from widgets.permits_by_month import permits_by_month
from widgets.sidebar import sidebar_filters
from widgets.tables.filtered import filtered_table
from widgets.tables.raw import raw_data_table

# Load processed data
# You can change this path if needed
DATA_PATH = 'output/processed_output.xlsx'

def main():
    # NOC 2011 Major Group names mapping (partial, add more as needed)
    st.title('Temporary Foreign Worker Permits Dashboard')

    with st.expander('About this Dashboard', expanded=False):
        st.markdown('''
    This dashboard shows the number of temporary work permits granted, broken down by occupation and month.
                
    Data Source: [Government of Canada Open Data](https://open.canada.ca/data/en/dataset/360024f2-17e9-4558-bfc1-3616485d65b9)  
                    ''')

    
    with st.expander('What are Temporary Foreign Worker Permits?', expanded=False):
        st.markdown('''
    **Temporary Foreign Worker Permits** (TFWPs) let Canadian employers hire foreign nationals to fill temporary labor shortages when no qualified Canadians or permanent residents are available.  
        
    
                
    Learn more: [Government of Canada - Temporary Foreign Worker Program](https://www.canada.ca/en/employment-social-development/services/foreign-workers.html)

        ''')

    
    
    # Load data
    df = pd.read_excel(DATA_PATH, index_col=0)

    
    selected_months, selected_occupations = sidebar_filters(df)

    st.info(f"Timeframe: {selected_months[0]} to {selected_months[-1]}\n\n**Tip:** You can adjust the filters in the sidebar to change the occupations and timeframe displayed.")

    filtered_df = df.loc[selected_occupations][selected_months]

    
    pie_chart_by_broad_category(filtered_df)

    permits_by_month(filtered_df, selected_months)

    filtered_table(filtered_df)

    raw_data_table(df)

if __name__ == '__main__':
    main()
