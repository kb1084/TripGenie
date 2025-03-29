def generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences):
    """Generate a structured travel itinerary."""
    itinerary = ""

    for i in range(trip_duration):
        itinerary += (
            f"\n📅 **Day {i+1}**\n"
            f"🎯 **Destination:** {destination}\n"
            f"💰 **Budget:** {budget} INR\n"
            f"🛫 **Starting From:** {start_location}\n"
            f"🎭 **Purpose:** {purpose}\n"
            f"🌟 **Preferences:** {preferences}\n\n"
            f"🌅 **Morning:** Explore a local attraction.\n"
            f"🍽️ **Afternoon:** Try a budget-friendly local restaurant.\n"
            f"🌆 **Evening:** Enjoy a cultural experience or nightlife.\n"
            f"🏨 **Stay:** Book a budget hotel.\n"
            f"🚖 **Transport:** Use local transport options.\n"
            f"📍 **Suggested Activities:** Visit famous landmarks and try local food.\n"
            "────────────────────────────\n"
        )
    
    return itinerary
