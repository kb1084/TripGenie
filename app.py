import streamlit as st
from datetime import date
from itinerary import generate_itinerary

st.title("🌍 TripGenie – Your AI Travel Genie!")

# Input Fields
budget = st.text_input("💰 Enter your budget (₹)", "1000")  # Added ₹ symbol
trip_duration = st.number_input("📅 Trip Duration (days)", min_value=1, max_value=30, value=5)
destination = st.text_input("📍 Enter your destination", "Paris")
start_location = st.text_input("🚀 Enter your starting location", "New York")
purpose = st.selectbox("🎯 Trip Purpose", ["Leisure", "Business", "Adventure", "Cultural"])
preferences = st.text_area("✨ Enter your preferences (e.g., food, sightseeing, adventure)", "Sightseeing, local food")

# Date Selection Feature
start_date = st.date_input("📆 Select your start date", date.today())

# Generate Itinerary Button
if st.button("🛫 Generate Itinerary"):
    itinerary = generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences, start_date)
    
    # Styled Output with Border
    st.subheader("📜 Here's an Itinerary Curated just for you!")
    st.markdown(
        f"""
        <div style="
            border: 2px solid #4CAF50;
            border-radius: 12px;
            padding: 20px;
            background-color: #f9f9f9;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            overflow-x: auto;
        ">
            <pre style="white-space: pre-wrap; font-size: 16px; line-height: 1.5; margin: 0; font-weight: 500;">{itinerary}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")  # Adds a separator line
st.markdown(f"""
<p style="text-align:center; font-size:16px;">
    Created with ❤️ by <b>Kaustubh Bhalerao</b>  
</p>
<p style="text-align:center;">
    <a href="https://www.linkedin.com/in/kaustubh-bhalerao-566a07258" target="_blank" style="text-decoration: none; font-weight: bold;">🔗 LinkedIn</a> 
    &nbsp;|&nbsp; 
    <a href="https://github.com/kb1084" target="_blank" style="text-decoration: none; font-weight: bold;">💻 GitHub</a>
</p>
""", unsafe_allow_html=True)
