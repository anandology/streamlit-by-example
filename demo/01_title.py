"""
**Title and Header**

The `st.title` function is used to create the
primary title heading of the page.

Typically this is the first thing you add to a page.

The `st.header` is used to create secondary headings in the page, typically one for each section.
"""
import streamlit as st

st.title("Hello, world!")

st.header("Section 1")
st.write("contents of section 1...")

st.header("Section 2")
st.write("contents of section 2...")
