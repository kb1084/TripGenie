import streamlit as st
from itinerary import generate_itinerary

st.title("🌍 TripGinie – Your AI Travel Genie!")

# Inputs
budget = st.text_input("💰 Enter your budget (₹)", "10000")
trip_duration = st.number_input("📅 Trip Duration (days)", min_value=1, max_value=30, value=5)
destination = st.text_input("📍 Enter your destination", "Delhi")
start_location = st.text_input("🚀 Enter your starting location", "Mumbai")
purpose = st.selectbox("🎯 Trip Purpose", ["Leisure", "Business", "Adventure", "Cultural"])
preferences = st.text_area("✨ Enter your preferences", "Sightseeing, local food")

# Debugging to check user input
st.write(f"🔍 **Debug:** Budget={budget}, Duration={trip_duration}, Destination={destination}")

# Generate Itinerary Button
if st.button("🛫 Generate Itinerary"):
    itinerary = generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences)
    
    # Debugging output
    st.write("🔍 **Debug:** Itinerary Generated ✅")

    # Display Itinerary
    if itinerary:
        st.subheader("📜 Your AI-Generated Itinerary")
        st.markdown(f"<pre style='white-space: pre-wrap; font-size: 16px;'>{itinerary}</pre>", unsafe_allow_html=True)
    else:
        st.error("⚠️ No itinerary generated! Check the function.")
