from ai_travel_model import query_huggingface

def generate_itinerary(budget, trip_duration, destination, start_location, purpose, preferences):
    """Generate a structured travel itinerary using Hugging Face API."""
    prompt = (
        f"Create a structured {trip_duration}-day travel itinerary from {start_location} to {destination}."
        f"\n\n### Trip Details:"
        f"\n- **Budget:** {budget} USD (strict, no deviations)"
        f"\n- **Purpose:** {purpose}"
        f"\n- **Preferences:** {preferences}"
        f"\n\n### Itinerary Requirements:"
        f"\n- Day-wise schedule with morning, afternoon, and evening activities"
        f"\n- Budget-friendly hotels"
        f"\n- Transportation options"
        f"\n- Local food recommendations"
        f"\n- Available tour guides or passes"
        f"\n- Ensure all expenses fit within the budget"
    )

    response = query_huggingface(prompt)

    return response if response else "❌ Error: Unable to fetch a valid itinerary from Hugging Face API."
