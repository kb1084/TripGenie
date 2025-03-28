import streamlit as st
from itinerary import generate_itinerary

st.title("🌍 TripGinie– Your AI Travel Genie!")

# Input Fields
budget = st.text_input("Enter your budget ($)", "1000")
trip_duration = st.number_input("Trip Duration (days)", min_value=1, max_value=30, value=5)
destination = st.text_input("Enter your destination", "Paris")
start_location = st.text_input("Enter your starting location", "New York")
purpose = st.selectbox("Trip Purpose", ["Leisure", "Business", "Adventure", "Cultural"])
preferences = st.text_area("Enter your preferences (e.g., food, sightseeing, adventure)", "Sightseeing, local food")

# Generate Itinerary Button
if st.button("Generate Itinerary"):
    itinerary = generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences)
    st.subheader("Generated Itinerary")
    st.write(itinerary)

# Footer
st.markdown("---")  # Adds a separator line
st.write("Created with ❤️ by **Kaustubh Bhalerao**")
st.write("[🔗 LinkedIn](https://www.linkedin.com/in/kaustubh-bhalerao-566a07258) | [💻 GitHub](https://github.com/kb1084)")
