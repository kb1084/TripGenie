from ai_travel_model import query_huggingface
from datetime import timedelta

def generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences, start_date):
    """Generate a structured travel itinerary using Hugging Face API with AI-generated day titles."""
    
    # Generate date-wise headers
    itinerary_dates = "\n".join(
        [f"- **Day {i+1} ({(start_date + timedelta(days=i)).strftime('%d %b %Y')})**"
         for i in range(trip_duration)]
    )

    prompt = (
        f"Create a structured {trip_duration}-day travel itinerary from {start_location} to {destination}."
        f"\n\n### Trip Details:"
        f"\n- **Start Date:** {start_date.strftime('%d %b %Y')}"
        f"\n- **Budget:** {budget} INR (strict, no deviations)"
        f"\n- **Purpose:** {purpose}"
        f"\n- **Preferences:** {preferences}"
        f"\n\n### Itinerary Requirements:"
        f"\n- Assign a unique and engaging **theme/title** for each day, reflecting the key activities planned."
        f"\n- The day titles should make the itinerary feel structured and exciting."
        f"\n- Here are the days with their respective dates (Generate unique titles for them):"
        f"\n{itinerary_dates}"
        f"\n- Day-wise schedule with morning, afternoon, and evening activities."
        f"\n- Budget-friendly hotels."
        f"\n- Transportation options."
        f"\n- Local food recommendations."
        f"\n- Available tour guides or passes."
        f"\n- Ensure all expenses fit within the budget."
    )

    response = query_huggingface(prompt)

    return response if response else "❌ Error: Unable to fetch a valid itinerary from Hugging Face API."
