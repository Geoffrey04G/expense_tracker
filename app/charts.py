import streamlit as st
import pandas as pd
import plotly.express as px
import os

DATA_PATH = "data/expenses/sampleuser.csv"

def load_expenses():
    import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def display_charts():
    st.markdown("<h2 style='color:#00ffee;'>📊 Expense by Category</h2>", unsafe_allow_html=True)

    # Dummy Data
    category_data = {
        'Food': 452,
        'Transport': 300,
        'Shopping': 780,
        'Bills': 210,
        'Health': 120,
        'Entertainment': 500
    }

    df = pd.DataFrame(list(category_data.items()), columns=['Category', 'Amount'])

    # Toggle for Pie/Bar
    chart_type = st.toggle("🌀 Switch to Pie Chart", value=False)

    if chart_type:
        # --- PIE CHART ---
        fig = go.Figure(
            data=[go.Pie(
                labels=df['Category'],
                values=df['Amount'],
                hole=0.45,
                pull=[0.08] * len(df),
                marker=dict(line=dict(color='#00ffee', width=2)),
                hovertemplate=(
                    '<span style="font-size:16px; color:#00ffee;"><b>%{label}</b></span><br>'
                    '<span style="font-size:14px; color:#ffffff;">Amount: ₹%{value}</span><extra></extra>'
                ),
                textinfo='label+percent'
            )]
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    else:
        # --- BAR CHART ---
        fig = go.Figure(
            data=[go.Bar(
                x=df['Category'],
                y=df['Amount'],
                marker=dict(
                    color='#00ffee',
                    line=dict(color='white', width=1.5)
                ),
                hovertemplate=(
                    '<span style="font-size:16px; color:#00ffee;"><b>%{x}</b></span><br>'
                    '<span style="font-size:14px; color:#ffffff;">Amount: ₹%{y}</span><extra></extra>'
                )
            )]
        )
        fig.update_layout(
            xaxis=dict(title='Category', tickfont=dict(color='#00ffee')),
            yaxis=dict(title='Amount', tickfont=dict(color='#00ffee')),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)
