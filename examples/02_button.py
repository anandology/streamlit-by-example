"""
## Button

The `st.button` creates a button and returns a boolean value whether or not the button is clicked.
"""

import streamlit as st

name = st.text_input("Enter your name")

button = st.button("Click me")
if button:
    st.write(name, "you clicked me!")

