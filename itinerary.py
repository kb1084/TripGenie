from ai_travel_model import query_huggingface
def generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences):
    print("✅ Function Called: generate_itinerary")
    print(f"📅 Duration: {trip_duration} days | 💰 Budget: {budget} | 📍 Destination: {destination}")
    
    if not budget or not trip_duration or not destination:
        return "⚠️ Error: Missing required inputs!"
    
    itinerary = ""
    
    for day in range(1, trip_duration + 1):
        itinerary += f"📅 **Day {day}** 🎯 **Destination:** {destination} 💰 **Budget:** {budget} INR 🛫 **Starting From:** {start_location} 🎭 **Purpose:** {purpose} 🌟 **Preferences:** {preferences}\n"
        itinerary += "🌅 Morning: Explore a local attraction.\n"
        itinerary += "🍽️ Afternoon: Try a budget-friendly local restaurant.\n"
        itinerary += "🌆 Evening: Enjoy a cultural experience or nightlife.\n"
        itinerary += "🏨 Stay: Book a budget hotel.\n"
        itinerary += "🚖 Transport: Use local transport options.\n"
        itinerary += "📍 Suggested Activities: Visit famous landmarks and try local food.\n"
        itinerary += "────────────────────────────\n"
    
    print("✅ Itinerary Generated Successfully!")
    return itinerary
