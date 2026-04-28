import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Climate Dashboard", layout="wide")
st.title("African Climate Data Dashboard")

st.sidebar.header("Controls")
country = st.sidebar.selectbox("Select Country:", ["Ethiopia", "Kenya", "Nigeria", "Sudan", "Tanzania"])

@st.cache_data
def load_data(country_name):
    path = f"data/{country_name.lower()}_clean.csv" 
    try:
        df = pd.read_csv(path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except FileNotFoundError:
        st.error(f"Could not find data for {country_name}. Please check the file path.")
        return pd.DataFrame() 

df = load_data(country)

if not df.empty:

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Temperature Trend in {country}")
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df['Date'], df['T2M'], color='red', linewidth=1)
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        ax.grid(True)
        st.pyplot(fig) 
    with col2:
        st.subheader(f"Key Statistics for {country}")
        avg_temp = df['T2M'].mean()
        max_temp = df['T2M_MAX'].max()
        st.metric("Average Temperature", f"{avg_temp:.1f} °C")
        st.metric("Recorded Maximum", f"{max_temp:.1f} °C")

else:
    st.warning("Please make sure the data files are in the 'data/' folder.")