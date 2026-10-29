import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_itinerary(destination: str, days: int, budget: str, interests: list) -> str:
    prompt = f"""
    You are an expert travel planner. Create a detailed, day-by-day travel itinerary for a trip to {destination}.
    
    Details:
    - Duration: {days} days
    - Budget Level: {budget}
    - User Interests: {', '.join(interests)}
    
    Provide a response structured as follows:
    1. Trip Summary & Overview
    2. Day-by-Day Breakdown (Morning, Afternoon, Evening) with specific activity & local food recommendations
    3. Estimated Budget Breakdown
    4. Essential Travel Tips (Local transport, safety, best times to visit)
    """

    # Use client.interactions.create with gemini-3.8-flash
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )
    return interaction.output_text