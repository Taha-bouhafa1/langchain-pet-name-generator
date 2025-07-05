import streamlit as st
import my_chain as mch
st.title("Pets Name Generator")

animal_type=st.sidebar.selectbox("What is your pet?",("Dog",
        "Cat",
        "Rabbit",
        "Hamster",
        "Cow",
        "Guinea Pig",
        "Parrot",
        "Budgie",
        "Canary",
        "Goldfish",
        "Betta Fish",
        "Turtle",
        "Tortoise",
        "Mouse",
        "Rat",
        "Lovebird",
        "Cockatiel"))
if animal_type:
    pet_color=st.sidebar.text_area(label=f"What color is your {animal_type}?",max_chars=15)
if pet_color:
    response=mch.generate_pet_name(animal_type,pet_color)
    st.text(response)