import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuCreate Streamlit Lab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Historical Scenario Stress Test Visualizer")
st.divider()

# Explanation of the Application
st.markdown("""
    ## Historical Scenario Stress Test Visualizer

    This application allows you to visualize how your portfolio might have performed during significant historical market events. 
    By selecting an event and defining your portfolio allocation, you can see interactive charts and key statistics 
    demonstrating potential impacts. This tool is designed for educational purposes to understand portfolio behavior 
    under stress conditions, as discussed in the context of risk management practices and stress testing.

    **How to use this application:**
    1. **Select a Historical Event:** Choose an event from the dropdown menu to analyze.
    2. **Define Portfolio Allocation:** Use the sliders to set the percentage allocation for each asset class in your portfolio.
    3. **Observe the Results:** View interactive visualizations and summary statistics that update in real-time based on your inputs.

    **Key Concepts:**
    - **Historical Scenario Stress Testing:** Re-enacting past market crises to quantify potential portfolio losses.
    - **Maximum Drawdown:** The largest peak-to-trough decline during a specific period.
    - **Portfolio Volatility:** A measure of the dispersion of returns for a given portfolio.

    **Note:** The data used in this application is synthetic and for illustrative purposes only. It is designed to mimic real-world 
    financial data patterns to demonstrate stress testing concepts.
    """)
st.divider()

# --- Data Generation ---
# Synthetic historical data - Self-sufficient dataset
@st.cache_data
def generate_synthetic_data():
    dates = pd.date_range(start="1987-01-01", end="2024-01-01", freq='M')
    events_data = {
        '1987 Crash': {
            'start_date': '1987-10-01', 'end_date': '1987-12-01',
            'Stocks': -0.30, 'Bonds': 0.05, 'Gold': 0.10
        },
        'Asian Crisis': {
            'start_date': '1997-07-01', 'end_date': '1998-01-01',
            'Stocks': -0.20, 'Bonds': 0.08, 'Gold': 0.15, 'Emerging Markets': -0.40
        },
        'Dot-com Bubble Burst': {
            'start_date': '2000-03-01', 'end_date': '2002-10-01',
            'Stocks': -0.45, 'Bonds': 0.15, 'Gold': 0.20, 'Technology': -0.60
        },
        '2008 Financial Crisis': {
            'start_date': '2008-09-01', 'end_date': '2009-03-01',
            'Stocks': -0.55, 'Bonds': 0.20, 'Gold': 0.25, 'Real Estate': -0.70, 'Credit': -0.50
        },
        'COVID-19 Pandemic': {
            'start_date': '2020-02-01', 'end_date': '2020-04-01',
            'Stocks': -0.35, 'Bonds': 0.10, 'Gold': 0.18, 'Oil': -0.80, 'Travel & Leisure': -0.65
        }
    }

    asset_classes = ['Stocks', 'Bonds', 'Gold', 'Emerging Markets', 'Technology', 'Real Estate', 'Credit', 'Oil', 'Travel & Leisure']
    df = pd.DataFrame({'Date': dates})
    for asset in asset_classes:
        df[asset] = 0.0  # Initialize all to zero change

    for event, event_data in events_data.items():
        start_event = pd.to_datetime(event_data['start_date'])
        end_event = pd.to_datetime(event_data['end_date'])
        event_period_mask = (df['Date'] >= start_event) & (df['Date'] <= end_event)
        for asset, impact in event_data.items():
            if asset in df.columns:
                df.loc[event_period_mask, asset] = impact

    df.set_index('Date', inplace=True)
    cumulative_returns_df = (1 + df).cumprod() - 1 # Cumulative returns
    return cumulative_returns_df, events_data

cumulative_returns_df, events_data = generate_synthetic_data()

# --- Sidebar Controls ---
st.sidebar.header("Stress Test Parameters")
historical_event = st.sidebar.selectbox("Select Historical Event", list(events_data.keys()))

st.sidebar.subheader("Portfolio Allocation")
asset_allocation = {}
available_assets = ['Stocks', 'Bonds', 'Gold'] # Base assets always available
if historical_event in events_data:
    event_assets = [asset for asset in events_data[historical_event] if asset in cumulative_returns_df.columns and asset not in available_assets]
    available_assets.extend(event_assets)

for asset in available_assets:
    if asset in ['Stocks', 'Bonds', 'Gold']: # Default assets are always shown
        default_weight = 30 if asset == 'Stocks' else (40 if asset == 'Bonds' else 30) # Example default allocation
    else:
        default_weight = 0
    asset_allocation[asset] = st.sidebar.slider(f"{asset} (%)", 0, 100, default_weight)

# Normalize weights to 100%
total_allocation = sum(asset_allocation.values())
if total_allocation > 0: # Avoid division by zero
    normalized_allocation = {asset: weight/total_allocation for asset, weight in asset_allocation.items()}
else:
    normalized_allocation = asset_allocation # If total is 0, keep as is (all zero weights)


# --- Portfolio Value Calculation ---
start_date = pd.to_datetime('1987-01-01') # Common start date for all scenarios
end_date = pd.to_datetime('2024-01-01') # Common end date for all scenarios

event_start_date = pd.to_datetime(events_data[historical_event]['start_date'])
event_end_date = pd.to_datetime(events_data[historical_event]['end_date'])

portfolio_value_df = pd.DataFrame(index=cumulative_returns_df.index)
portfolio_value_df['Portfolio Value'] = 100 # Initial portfolio value

# Calculate portfolio returns based on allocation and historical event data
for index, row in cumulative_returns_df.iterrows():
    portfolio_return = 0
    for asset, weight in normalized_allocation.items():
        if asset in row.index: # Ensure asset exists in the data for the selected event
            portfolio_return += weight * row[asset]

    if index > portfolio_value_df.index[0]: # Start from the second date to calculate change
        previous_value = portfolio_value_df['Portfolio Value'].shift(1).fillna(100)[index] # Get previous value, default to 100 for first period
        portfolio_value_df.loc[index, 'Portfolio Value'] = previous_value * (1 + portfolio_return)
    else:
        pass # Initial value already set to 100

# --- Visualizations ---
st.header(f"Portfolio Performance During: {historical_event}")

# Line Chart of Portfolio Value
st.subheader("Portfolio Value Over Time")
st.caption("This chart visualizes the growth or decline of your portfolio value during the selected historical event and the periods around it. Observe how the portfolio reacts to market stresses.")

fig_portfolio_value = px.line(portfolio_value_df, x=portfolio_value_df.index, y='Portfolio Value',
                             title=f"Portfolio Value Trend during {historical_event}",
                             labels={'Portfolio Value': 'Portfolio Value (Starting at 100)'})
fig_portfolio_value.add_vrect(x0=event_start_date, x1=event_end_date,
                             fillcolor="red", opacity=0.1,
                             annotation_text=historical_event, annotation_position="top left")
st.plotly_chart(fig_portfolio_value, use_container_width=True)


# Bar Chart of Asset Class Contribution during Event Period
st.subheader("Asset Class Performance Contribution during Event")
st.caption("This bar chart shows the contribution of each asset class to the overall portfolio performance during the selected historical event. Negative contributions indicate losses, while positive contributions show gains. This helps in understanding which assets were most affected.")

event_returns = cumulative_returns_df[(cumulative_returns_df.index >= event_start_date) & (cumulative_returns_df.index <= event_end_date)].iloc[-1] # Returns at the end of the event
asset_contributions = {}
for asset, weight in normalized_allocation.items():
    if asset in event_returns.index:
        asset_contributions[asset] = weight * event_returns[asset]

if asset_contributions: # Check if there is any contribution to plot
    contribution_df = pd.DataFrame(list(asset_contributions.items()), columns=['Asset Class', 'Contribution'])
    fig_asset_contribution = px.bar(contribution_df, x='Asset Class', y='Contribution',
                                    title="Asset Contribution to Portfolio Return during Event",
                                    labels={'Contribution': 'Return Contribution'})
    st.plotly_chart(fig_asset_contribution, use_container_width=True)
else:
    st.write("No asset contribution data available for the selected portfolio and event.")


# --- Summary Statistics ---
st.subheader("Portfolio Summary Statistics")
st.caption("Key performance metrics during the selected historical event are calculated below. These metrics provide a quantitative summary of the portfolio's stress test performance.")

event_portfolio_values = portfolio_value_df[(portfolio_value_df.index >= event_start_date) & (portfolio_value_df.index <= event_end_date)]

# Maximum Drawdown Calculation
peak_value = event_portfolio_values['Portfolio Value'].cummax()
drawdown = (event_portfolio_values['Portfolio Value'] - peak_value) / peak_value
max_drawdown = drawdown.min()

# Portfolio Volatility Calculation (using daily returns during event for simplicity - could be annualized)
event_daily_returns = event_portfolio_values['Portfolio Value'].pct_change().dropna()
portfolio_volatility = event_daily_returns.std() * np.sqrt(252) # Annualize volatility - using trading days approximation


col1, col2 = st.columns(2)
with col1:
    st.metric("Maximum Drawdown", f"{max_drawdown:.2%}", help="Maximum percentage decline from a peak to a trough during the event period.")
with col2:
    st.metric("Annualized Volatility (during event)", f"{portfolio_volatility:.2%}", help="Annualized standard deviation of portfolio returns during the event period, indicating risk level.")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
