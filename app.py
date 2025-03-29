import streamlit as st
from itinerary import generate_itinerary

# App Title
st.title("🌍 TripGinie – Your AI Travel Genie!")

# Input Fields with Icons
budget = st.text_input("💰 Enter your budget (₹)", "1000")
trip_duration = st.number_input("📅 Trip Duration (days)", min_value=1, max_value=30, value=5)
destination = st.text_input("📍 Enter your destination", "Paris")
start_location = st.text_input("🚀 Enter your starting location", "New York")
purpose = st.selectbox("🎯 Trip Purpose", ["Leisure", "Business", "Adventure", "Cultural"])
preferences = st.text_area("✨ Enter your preferences (e.g., food, sightseeing, adventure)", "Sightseeing, local food")

# Generate Itinerary Button
if st.button("🛫 Generate Itinerary"):
    itinerary = generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences)

    # Stylish Output Box
    st.subheader("📜 Your AI-Generated Itinerary")
    st.markdown(
        f"""
        <div style="
            border: 2px solid #4CAF50;
            border-radius: 12px;
            padding: 20px;
            background-color: #ffffff;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.1);
            line-height: 1.5;
        ">
            <pre style="white-space: pre-wrap; font-size: 16px; margin: 0;">{itinerary}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer
st.markdown("---")  # Separator Line
st.markdown(
    """
    <div style="text-align:center; font-size:16px;">
        Created with ❤️ by <b>Kaustubh Bhalerao</b><br>
        <a href="https://www.linkedin.com/in/kaustubh-bhalerao-566a07258" target="_blank" 
            style="text-decoration: none; font-weight: bold; color: #0077b5;">🔗 LinkedIn</a> 
        &nbsp;|&nbsp; 
        <a href="https://github.com/kb1084" target="_blank" 
            style="text-decoration: none; font-weight: bold; color: #333;">💻 GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
