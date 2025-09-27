import streamlit as st
import plotly.graph_objects as go

def permits_by_month(filtered_df, selected_months):
    # Show a chart (sum by month)
    st.subheader('Total Permits by Month')
    st.markdown('Drag to zoom in on specific time periods. Double-click to reset zoom.')
    # Ensure months are sorted chronologically
    month_totals = filtered_df.sum(axis=0).reindex(selected_months)

    fig_month = go.Figure(go.Bar(x=month_totals.index, y=month_totals.values))
    fig_month.update_layout(xaxis_title='Month', yaxis_title='Total Permits')
    st.plotly_chart(fig_month, use_container_width=True)