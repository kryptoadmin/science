import streamlit as st
import pandas as pd

st.title("Streamlit widgets")

name = st.text_input("Enter your name:") # Textbox widget
if name:
    st.write(f"Hi, {name}!!!")

age = st.slider("Enter your age", 1, 100, 25) # Slider widget
if age:
    st.write(f"Are you {age} years old?")

programming_languages = ["Python", "Java", "Go", "Draft", "Ruby"]
fav = st.selectbox("Select your favorite programming language", programming_languages) # Selectbox widget
st.write(f"Your favorite programming language seems to be {fav}")

df = pd.DataFrame(
    {
        "names": ["Dilip", "Keerthi", "Anusha", "Lavanya", "Deepthi", "Sandhya"],
        "ages": [40,41,39,38,36, 38],
        "natives": ["Kadapa", "Kadapa", "Kerala", "Bangalore", "Hosur", "Rayadurgham"]
    }
)

st.write("Data frame:")
st.write(df)

## Upload a file
uploaded = st.file_uploader("Upload csv file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df)