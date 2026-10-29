import streamlit as st
from generator import generate_itinerary

st.set_page_config(page_title="AI Travel Itinerary Planner", page_icon="✈️", layout="centered")

st.title("✈️ Personalized Travel Itinerary Planner")
st.write("Plan your custom trip in seconds using Google Generative AI.")

with st.form("itinerary_form"):
    destination = st.text_input("Destination City / Country", placeholder="e.g., Kyoto, Japan")
    days = st.number_input("Number of Days", min_value=1, max_value=14, value=3)
    budget = st.selectbox("Budget Level", ["Budget-Friendly", "Moderate", "Luxury"])
    
    interests = st.multiselect(
        "Interests & Preferences",
        ["Culture & History", "Food & Cuisine", "Adventure & Nature", "Shopping", "Relaxation", "Nightlife"],
        default=["Culture & History", "Food & Cuisine"]
    )
    
    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    if not destination.strip():
        st.error("Please enter a destination.")
    else:
        with st.spinner("Crafting your personalized itinerary..."):
            try:
                result = generate_itinerary(destination, days, budget, interests)
                st.success("Itinerary Ready!")
                st.markdown(result)
            except Exception as e:
                st.error(f"Error generating itinerary: {e}")