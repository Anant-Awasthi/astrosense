import streamlit as st
import plotly.express as px
from data_fetcher import fetch_nasa_space_weather
from ai_specialist import generate_ai_briefing

st.set_page_config(
    page_title="AstroSense | Space Weather & Launch Risk",
    page_icon="🚀",
    layout="wide"
)

# --- CUSTOM CSS FOR NASA SPACE CONTROL DARK MODE ---
st.markdown("""
    <style>
    /* Dark Space Theme Background */
    .stApp {
        background-color: #0B0E14;
        color: #E2E8F0;
    }
    
    /* Card Container styling */
    div[data-testid="stMetric"] {
        background: rgba(22, 27, 38, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    
    /* Custom Sidebar / Container Borders */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 12px;
    }

    /* Primary Accent Color for Labels */
    div[data-testid="stMetricLabel"] > label {
        color: #94A3B8 !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Glowing Stat Values */
    div[data-testid="stMetricValue"] {
        color: #F8FAFC !important;
        font-family: 'Inter', monospace;
        font-weight: 700 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col_head, col_btn = st.columns([4, 1])
with col_head:
    st.title("🚀 AstroSense")
    st.caption("Powered by IBM Bob | Real-Time NASA DONKI Space Telemetry & AI Launch Risk Engine")

with col_btn:
    st.write(" ")
    if st.button("🔄 Sync NASA Live Data", use_container_width=True):
        st.cache_data.clear()

st.divider()

# --- FETCH NASA DATA ---
with st.spinner("Fetching live telemetry from NASA DONKI API..."):
    metrics, forecast_df = fetch_nasa_space_weather()
    current_risk = forecast_df["Risk_Score"].iloc[0]

# --- METRICS BAR ---
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Launch Risk Index", f"{current_risk:.1f}%")
m2.metric("Solar Flare Class", metrics["solar_flare"])
m3.metric("Geomagnetic Kp-Index", f"{metrics['kp_index']} / 9")
m4.metric("Solar Wind Speed", f"{metrics['solar_wind_speed']} km/s")
m5.metric("Proton Radiation Flux", f"{metrics['proton_flux']} p/cm²")

st.divider()

# --- MAIN DASHBOARD GRID ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 24-Hour Predictive Launch Window Risk Curve")
    
    fig = px.line(
        forecast_df, 
        x="Timestamp", 
        y="Risk_Score",
        labels={"Risk_Score": "Risk Score (%)", "Timestamp": "Time (UTC)"}
    )
    
    # Styling plot for Space Dark Mode
    fig.update_traces(line_color="#38BDF8", line_width=2.5)
    fig.add_hrect(y0=70, y1=100, fillcolor="#EF4444", opacity=0.18, line_width=0, annotation_text="NO-GO Zone", annotation_position="top right")
    fig.add_hrect(y0=40, y1=70, fillcolor="#F59E0B", opacity=0.18, line_width=0, annotation_text="Caution Zone", annotation_position="top right")
    fig.add_hrect(y0=0, y1=40, fillcolor="#10B981", opacity=0.18, line_width=0, annotation_text="GO Zone", annotation_position="top right")
    
    fig.update_layout(
        height=380,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font=dict(color="#94A3B8"),
        xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", range=[0, 100])
    )
    
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.subheader("🤖 IBM Bob AI Mission Specialist")
    briefing = generate_ai_briefing(metrics, current_risk)
    
    with st.container(border=True):
        st.markdown(f"### Status: {briefing['status']}")
        st.markdown(f"**Analysis:** {briefing['recommendation']}")
        st.info(f"**Action Plan:** {briefing['action']}")
        
    st.caption(f"🛰️ Live NASA Sync: {metrics['last_updated']}")