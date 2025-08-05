
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.model_utils import get_available_models, load_model, generate_forecast

st.set_page_config(page_title="Favorita Forecasting", layout="wide")
st.title("📦 AI-Powered Sales Forecasting Dashboard")

# -- Load available model options
models = get_available_models("notebooks/models")
stores = sorted(set([s for s, _ in models]))
families = sorted(set([f for _, f in models]))

# -- Sidebar Inputs
st.sidebar.header("Forecast Controls")

store = st.sidebar.selectbox("Select Store", stores, index=stores.index(44) if 44 in stores else 0)
family = st.sidebar.selectbox("Select Family", families, index=families.index("BEVERAGES") if "BEVERAGES" in families else 0)
horizon = st.sidebar.slider("Forecast Horizon (days)", min_value=7, max_value=180, value=60)
promo_toggle = st.sidebar.checkbox("On Promotion", value=False)
holiday_toggle = st.sidebar.checkbox("Holiday Period", value=False)

# -- Load model and generate forecast
try:
    model = load_model(store, family, model_dir="notebooks/models")
    future_df, hist_df = generate_forecast(
    model, 
    horizon_days=horizon, 
    promo=int(promo_toggle), 
    holiday=int(holiday_toggle),
    return_split=True)

    # -- Plot forecast
    st.subheader(f"📈 Forecast for Store {store} — {family}")

    fig, ax = plt.subplots(figsize=(12, 5))
    # Actuals: last 30 days
    ax.plot(hist_df['ds'].tail(30), hist_df['yhat'].tail(30), 'k.', label="Recent Actuals (approx)")

    # Future forecast
    ax.plot(future_df['ds'], future_df['yhat'], label="Forecast", color='blue')
    ax.fill_between(future_df['ds'], future_df['yhat_lower'], future_df['yhat_upper'], alpha=0.2)

    # Forecast line marker
    ax.axvline(x=hist_df['ds'].max(), color='red', linestyle='--', label='Forecast Start')
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.legend()
    st.pyplot(fig)

    # -- Show forecast table
    st.markdown("### 🔍 Forecast Data (Future Only)")
    st.dataframe(future_df[['ds', 'yhat', 'onpromotion', 'is_holiday', 'day_of_week', 'is_weekend']].reset_index(drop=True))

except Exception as e:
    st.error(f"⚠️ Error loading forecast: {e}")
