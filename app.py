import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 African Climate Data Dashboard")

st.sidebar.header("Controls")
country = st.sidebar.selectbox("Select Country:", ["Ethiopia", "Kenya", "Sudan", "Nigeria", "Tanzania"])

# Year range slider
st.sidebar.subheader("Filter by Year")
years = st.sidebar.slider(
    "Select Year Range",
    min_value=2015,
    max_value=2026,
    value=(2015, 2026)
)

@st.cache_data
def load_data(country_name):
    # Special case for Ethiopia
    if country_name == "Ethiopia":
        path = "data/ethiopia_clean.csv"
    else:
        path = f"data/{country_name.lower()}_clean.csv"
    
    if os.path.exists(path):
        df = pd.read_csv(path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    else:
        st.error(f"File not found: {path}")
        return pd.DataFrame()

df = load_data(country)

if not df.empty:
    # Filter by year range
    df = df[(df['Date'].dt.year >= years[0]) & (df['Date'].dt.year <= years[1])]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"📈 Temperature Trend in {country}")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df['Date'], df['T2M'], color='red', linewidth=1)
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    
    with col2:
        st.subheader(f"📊 Key Statistics for {country}")
        avg_temp = df['T2M'].mean()
        max_temp = df['T2M_MAX'].max()
        min_temp = df['T2M_MIN'].min()
        st.metric("Average Temperature", f"{avg_temp:.1f} °C")
        st.metric("Highest Recorded", f"{max_temp:.1f} °C")
        st.metric("Lowest Recorded", f"{min_temp:.1f} °C")
    
    # Precipitation boxplot
    st.subheader(f"💧 Precipitation Distribution in {country}")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.boxplot(df['PRECTOTCORR'].dropna())
    ax2.set_ylabel("Precipitation (mm/day)")
    ax2.set_title(f"Daily Precipitation Distribution in {country}")
    st.pyplot(fig2)
else:
    st.warning("Please make sure the data files are in the 'data/' folder.")