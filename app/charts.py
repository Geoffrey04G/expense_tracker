# app/charts.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

def display_charts():
    from app.expense_manager import load_expenses
    st.markdown("<h2 style='color:#00ffee;'>📊 Expense by Category</h2>", unsafe_allow_html=True)
    df = load_expenses()
    if df.empty:
        st.info("No expense data to visualize.")
        return

    category_data = df.groupby("Category")["Amount"].sum().to_dict()
    df_plot = pd.DataFrame(list(category_data.items()), columns=['Category', 'Amount'])

    chart_type = st.toggle("🌀 Switch to Pie Chart", value=False)

    if chart_type:
        fig = go.Figure(data=[go.Pie(
            labels=df_plot['Category'],
            values=df_plot['Amount'],
            hole=0.45,
            pull=[0.08] * len(df_plot),
            marker=dict(line=dict(color='#00ffee', width=2)),
            hovertemplate=(
                '<span style="font-size:16px; color:#00ffee;"><b>%{label}</b></span><br>'
                '<span style="font-size:14px; color:#ffffff;">Amount: ₹%{value}</span><extra></extra>'
            ),
            textinfo='label+percent'
        )])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
    else:
        colors = ['#00ffee', '#ff00ff', '#00ff88', '#ff4444', '#8888ff', '#ffaa00']
        fig = go.Figure(data=[go.Bar(
            x=df_plot['Category'],
            y=df_plot['Amount'],
            marker=dict(color=colors[:len(df_plot)], line=dict(color='white', width=1.5)),
            hovertemplate=(
                '<span style="font-size:16px; color:#00ffee;"><b>%{x}</b></span><br>'
                '<span style="font-size:14px; color:#ffffff;">Amount: ₹%{y}</span><extra></extra>'
            )
        )])
        fig.update_layout(
            xaxis=dict(title='Category', tickfont=dict(color='#00ffee')),
            yaxis=dict(title='Amount', tickfont=dict(color='#00ffee')),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#ffffff'),
            margin=dict(t=20, b=20, l=20, r=20)
        )
        st.plotly_chart(fig, use_container_width=True)
